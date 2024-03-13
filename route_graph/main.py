"""Main part of route-graph."""
import ipaddress
import shutil
from pathlib import Path
from typing import Optional

import typer
from scapy.all import traceroute
from typing_extensions import Annotated

from route_graph.exceptions import BinaryNotFoundError

app = typer.Typer()


def validate(address: str):
    """Check if graphviz is available and if IP address is valid."""
    if shutil.which("dot") is None:
        raise BinaryNotFoundError("graphviz is not installed")

    try:
        ipaddress.ip_address(address)
    except ValueError:
        raise typer.BadParameter("URL is not valid")
    return address


@app.callback()
def callback():
    """Tool to draw a graph of traceroute results."""


@app.command()
def graph(
    target: Annotated[str, typer.Argument(callback=validate)],
    path: Annotated[
        Optional[Path],
        typer.Option(help="Path to store the exported files"),
    ] = ".",
):
    """Create a graph from traceroute results."""
    typer.echo("Collect details ...")
    res, unans = traceroute([target], dport=[80, 443], maxttl=20, retry=-2)
    output_string = Path(path) / Path(f"{target}.png")
    res.graph(target=f"> {output_string}")
