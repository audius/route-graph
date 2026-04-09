"""Tests for route_graph.exceptions module."""
import pytest

from route_graph.exceptions import BinaryNotFoundError


class TestBinaryNotFoundError:
    """Tests for the BinaryNotFoundError exception."""

    def test_exception_can_be_raised(self):
        """Test that the exception can be raised."""
        with pytest.raises(BinaryNotFoundError):
            raise BinaryNotFoundError("test error")

    def test_exception_message(self):
        """Test that the exception contains the correct message."""
        with pytest.raises(BinaryNotFoundError) as exc_info:
            raise BinaryNotFoundError("graphviz is not installed")
        assert str(exc_info.value) == "graphviz is not installed"

    def test_exception_inherits_from_exception(self):
        """Test that BinaryNotFoundError inherits from Exception."""
        assert issubclass(BinaryNotFoundError, Exception)

    def test_exception_without_message(self):
        """Test that the exception can be raised without a message."""
        with pytest.raises(BinaryNotFoundError):
            raise BinaryNotFoundError()
