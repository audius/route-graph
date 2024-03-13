# route-graph

CLI tool for creating graphs of routes.

This tool simply wraps the example of [TCP traceroute](https://scapy.readthedocs.io/en/latest/usage.html#tcp-traceroute-2)
which is mentioned in the `scapy` documentation.

## Requirements

You will need `graphviz` to be installed. If `graphviz` is not available
on your system the graph can be created.

`route-graph` has to be executed with `sudo`.

## Installation

The package is available in the [Python Package Index](https://pypi.org/project/route-graph/).

```bash
$ pip3 install route-graph --user
```

To get the lastest state:

```bash
$ pip install git+https://github.com/audiusGmbH/route-graph.git
```

For Nix or NixOS users is a [package](https://search.nixos.org/packages?channel=unstable&from=0&size=50&sort=relevance&type=packages&query=route-graph)
available in Nixpkgs. Keep in mind that the lastest releases might only
be present in the ``unstable`` channel.

```bash
$ nix-env -iA nixos.route-graph
```

## Usage

```bash
$ sudo ./route-graph --help
                                                                                                                       
 Usage: route-graph [OPTIONS] COMMAND [ARGS]...                                                                        
                                                                                                                       
 Tool to draw a graph of traceroute results.                                                                           
                                                                                                                       
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                             │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.      │
│ --help                        Show this message and exit.                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ graph           Create a graph from traceroute results.                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

The graph could then be found in the current directory. The format is `png`.

## License

`route-graph` is licensed under MIT, for more details check the LICENSE file.
