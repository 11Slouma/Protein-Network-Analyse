# Protein-Network-Analyse
This repository contains the Python code for analyzing protein interaction networks.
## Installation
```
python 3.12
```
### Library
The following libraries are required to run this code:
* `random`
* `heapq`
## Porject description
This Python code implements an algorithm to analyze random protein networks generated from a file of protein names. The network is then analyzed to determine whether it has the characteristics of a "small world".
### Code features :
The code provided includes the following features:
* `read_proteins(file_name)`: Reads protein names from the specified text file `file_name` and returns a list containing the protein names.
* `generate_random_network(proteins, num_interactions)`: Creates a random network of proteins from the list `proteins` and the number of interactions `num_interactions`. The network is represented as a list of pairs of protein names (connected nodes).
* `write_network_data(file_name, network)`: Writes the `network` to the specified text file `file_name`, with each interaction represented by two protein names separated by a hyphen.
* `read_network_data(file_name)`: Reads network data from the text file `file_name` and returns a list of strings representing the interactions.
* `dijkstra(graph, start)`: Implements Dijkstra's algorithm to calculate the shortest distance between the `start` node and all other nodes in the `graph`. The function returns a dictionary where the key is a node and the value is its shortest distance from the start node.
* `clustering_coefficient(graph, node)`: Calculates the clustering coefficient of node `node` in the `graph`. The clustering coefficient represents the proportion of connected triplets centered on the `node`.
* `average_shortest_path_length(graph)`: Calculates the average characteristic distance of the `graph`. The characteristic distance is the average length of the shortest path between two random nodes.
* `is_small_world(graph)`: Determines whether the `graph` has the characteristics of a "small world". A "small world" network has a short characteristic distance and a high clustering coefficient. The function returns `True` if the network is "small-world" and `False` otherwise.
* `node_degree(network, node)`: Calculates the degree of the `node` in the `network`. The degree of a node is the number of links connected to it.
## Additional Notes

* This code can be further extended to include features like:
    * Loading protein interaction data from other sources (e.g., databases).
    * Implementing different network analysis algorithms.
    * Adding functionalities for network comparison and clustering.
