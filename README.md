# Open-RAN-xApp-Conflict-Graph-Generator

This repository contains the Python code for generating conflict graphs for xApps in an Open-RAN network. The script utilizes NetworkX to create a graph that visualizes potential conflicts between xApps based on their shared control parameters (ICPs).

![Conflict_Graph_ex](https://github.com/nimaafraz/Open-RAN-xApp-Conflict-Graph-Generator/assets/10645821/8f9aa019-fa1f-4c7b-b577-a728c91e58d9)

## Description

The script `conflict_graph_code.py` reads in a table of xApps with their respective ICPs and objectives, and constructs a graph where each node represents an xApp, and an edge indicates a potential conflict. This graph helps in identifying where conflicts may arise when xApps attempt to modify the same parameters simultaneously.

## Dependencies

- Python 3.6 or higher
- NetworkX
- Matplotlib
- Pandas

## Installation

To run this script, you need to have Python installed on your system. If you do not have Python installed, you can download it from the [official website](https://www.python.org/downloads/).

After installing Python, you can install the required libraries using pip:

```bash
pip install networkx matplotlib pandas
```
The script will produce a visual graph output that illustrates the xApps conflicts within the Open-RAN network.

## Input Data Format
The input data should be structured in a specific format for the script to process correctly. Ensure that you have a CSV or a similar data file that contains the following columns:

![image](https://github.com/nimaafraz/Open-RAN-xApp-Conflict-Graph-Generator/assets/10645821/efd78f76-086a-4e68-b106-6946986217cc)

**Name**: Name of the xApp
**ICPs**: List of control parameters that the xApp will adjust
An example of the expected input format is provided within the repository.

## References

- Abdul Wadud, Fatemeh Golpayegani, and Nima Afraz. "Conflict Management in the Near-RT-RIC of Open RAN: A Game Theoretic Approach." 2023. [arXiv:2311.13389](https://arxiv.org/abs/2311.13389)

## Contributing
If you would like to contribute to this project or have any suggestions for improvements, please feel free to open an issue or a pull request.

