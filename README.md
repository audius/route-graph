# route-graph

CLI tool for creating graphs of routes.

This tool simply wraps the example of [TCP traceroute](https://scapy.readthedocs.io/en/latest/usage.html#tcp-traceroute-2)
which is mentioned in the `scapy` documentation.

## Requirements

You will need `graphviz` to be installed. If `graphviz` is not available
on your system the graph can be created.

`route-graph` has to be executed with `sudo`.

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
