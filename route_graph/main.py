"""Main part of route-graph."""
import ipaddress
import shutil

import typer
from scapy.all import traceroute
from typing_extensions import Annotated

app = typer.Typer()

path = shutil.which("dot")


def validate(address: str):
    """Check if graphviz is available and if IP address is valid."""
    if path is None:
        typer.echo("graphviz is not installed")

    try:
        ipaddress.ip_address(address)
    except ValueError:
        raise typer.BadParameter("URL is not valid")
    return address


@app.callback()
def callback():
    """Tool to draw a graph of traceroute results."""


@app.command()
def graph(target: Annotated[str, typer.Argument(callback=validate)]):
    """Create a graph from traceroute results."""
    typer.echo("Collect details ...")
    res, unans = traceroute([target], dport=[80, 443], maxttl=20, retry=-2)
    res.graph(target=f"> {target}-graph.png")
