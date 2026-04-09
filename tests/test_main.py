"""Tests for route_graph.main module."""
import pytest
import typer
from typer.testing import CliRunner
from unittest.mock import patch, MagicMock

from route_graph.main import validate, version, app, __version__
from route_graph.exceptions import BinaryNotFoundError


runner = CliRunner()


class TestValidate:
    """Tests for the validate function."""

    def test_valid_ipv4_address(self):
        """Test that a valid IPv4 address passes validation."""
        result = validate("192.168.1.1")
        assert result == "192.168.1.1"

    def test_valid_ipv6_address(self):
        """Test that a valid IPv6 address passes validation."""
        result = validate("::1")
        assert result == "::1"

    def test_valid_ipv6_full_address(self):
        """Test that a full IPv6 address passes validation."""
        result = validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334")
        assert result == "2001:0db8:85a3:0000:0000:8a2e:0370:7334"

    def test_invalid_ip_address(self):
        """Test that an invalid IP address raises BadParameter."""
        with pytest.raises(typer.BadParameter, match="URL is not valid"):
            validate("invalid-ip")

    def test_invalid_ip_with_extra_octets(self):
        """Test that an IP with too many octets raises BadParameter."""
        with pytest.raises(typer.BadParameter, match="URL is not valid"):
            validate("192.168.1.1.1")

    def test_invalid_ip_out_of_range(self):
        """Test that an IP with out-of-range values raises BadParameter."""
        with pytest.raises(typer.BadParameter, match="URL is not valid"):
            validate("256.256.256.256")

    def test_empty_string(self):
        """Test that an empty string raises BadParameter."""
        with pytest.raises(typer.BadParameter, match="URL is not valid"):
            validate("")

    def test_hostname_not_allowed(self):
        """Test that hostnames are not allowed, only IPs."""
        with pytest.raises(typer.BadParameter, match="URL is not valid"):
            validate("example.com")


class TestVersion:
    """Tests for the version callback."""

    def test_version_flag_exits(self):
        """Test that the version callback exits when value is True."""
        with pytest.raises(typer.Exit):
            version(True)

    def test_version_flag_false_does_nothing(self):
        """Test that the version callback does nothing when value is False."""
        result = version(False)
        assert result is None

    def test_version_flag_none_does_nothing(self):
        """Test that the version callback does nothing when value is None."""
        result = version(None)
        assert result is None


class TestCLI:
    """Tests for the CLI app."""

    @patch("route_graph.main.shutil.which")
    def test_app_without_graphviz_raises_error(self, mock_which):
        """Test that the app raises BinaryNotFoundError if graphviz is missing."""
        mock_which.return_value = None
        result = runner.invoke(app, ["graph", "8.8.8.8"])
        assert result.exit_code != 0
        assert isinstance(result.exception, BinaryNotFoundError)
        assert "graphviz is not installed" in str(result.exception)

    @patch("route_graph.main.shutil.which")
    def test_version_option(self, mock_which):
        """Test the --version option."""
        mock_which.return_value = "/usr/bin/dot"
        result = runner.invoke(app, ["--version"])
        assert result.exit_code == 0
        assert f"Version: {__version__}" in result.output

    @patch("route_graph.main.traceroute")
    @patch("route_graph.main.shutil.which")
    def test_graph_command_with_valid_ip(self, mock_which, mock_traceroute):
        """Test the graph command with a valid IP address."""
        mock_which.return_value = "/usr/bin/dot"
        mock_res = MagicMock()
        mock_traceroute.return_value = (mock_res, [])
        
        result = runner.invoke(app, ["graph", "8.8.8.8"])
        
        assert "Collect details" in result.output
        mock_traceroute.assert_called_once()
        mock_res.graph.assert_called_once()

    @patch("route_graph.main.shutil.which")
    def test_graph_command_with_invalid_ip(self, mock_which):
        """Test the graph command with an invalid IP address."""
        mock_which.return_value = "/usr/bin/dot"
        result = runner.invoke(app, ["graph", "invalid-ip"])
        assert result.exit_code != 0
        assert "URL is not valid" in result.output

    @patch("route_graph.main.traceroute")
    @patch("route_graph.main.shutil.which")
    def test_graph_command_with_custom_path(self, mock_which, mock_traceroute):
        """Test the graph command with a custom output path."""
        mock_which.return_value = "/usr/bin/dot"
        mock_res = MagicMock()
        mock_traceroute.return_value = (mock_res, [])
        
        result = runner.invoke(app, ["graph", "8.8.8.8", "--path", "/tmp"])
        
        assert result.exit_code == 0
        mock_res.graph.assert_called_once()
        call_args = mock_res.graph.call_args
        assert "/tmp" in call_args[1]["target"]
