#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:40:04 2024

@author: aymen
"""

import random
import heapq

# Fonction pour lire les protéines à partir du fichier 'prot.txt'
def read_proteins(file_name):
    with open(file_name, 'r') as file:
        proteins = file.read().split()
    return proteins

# Fonction pour générer aléatoirement les interactions du réseau à partir des protéines
def generate_random_network(proteins, num_interactions):
    network = []
    num_proteins = len(proteins)
    for _ in range(num_interactions):
        node1 = random.choice(proteins)
        node2 = random.choice(proteins)
        while node1 == node2:
            node2 = random.choice(proteins)
        network.append((node1, node2))
    return network

# Fonction pour écrire les données du réseau dans le fichier 'proteines.txt'
def write_network_data(file_name, network):
    with open(file_name, 'w') as file:
        for interaction in network:
            file.write(f"{interaction[0]}-{interaction[1]} ")
        file.write("\n")

# Fonction pour lire les données du fichier 'proteines.txt'
def read_network_data(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
    return data

# Algorithme de Dijkstra pour trouver la plus courte distance entre deux nœuds dans un graphe pondéré ou non pondéré
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Calcul du coefficient de clustering d'un nœud dans un graphe non orienté
def clustering_coefficient(graph, node):
    neighbors = graph[node]
    if len(neighbors) < 2:
        return 0.0

    total_triangles = 0
    for neighbor1 in neighbors:
        for neighbor2 in neighbors:
            if neighbor1 != neighbor2 and (node, neighbor1) in graph and (node, neighbor2) in graph:
                total_triangles += 1

    possible_triangles = len(neighbors) * (len(neighbors) - 1) / 2
    if possible_triangles == 0:
        return 0.0
    else:
        return total_triangles / possible_triangles

# Calcul du chemin le plus court moyen dans un graphe pondéré ou non pondéré
def average_shortest_path_length(graph):
    total_path_length = 0
    num_paths = 0
    for node in graph:
        distances = dijkstra(graph, node)
        for target in distances:
            if distances[target] != 0 and distances[target] != float('inf'):
                total_path_length += distances[target]
                num_paths += 1
    if num_paths == 0:
        return float('inf')
    else:
        return total_path_length / num_paths

# Détermination si le réseau est de type Small World
def is_small_world(graph):
    avg_shortest_path = average_shortest_path_length(graph)
    avg_clustering_coefficient = sum(clustering_coefficient(graph, node) for node in graph) / len(graph)
    
    # Seuils pour déterminer si le réseau est de type Small World
    seuil1 = 2
    seuil2 = 0.1
    
    if avg_shortest_path <= seuil1 and avg_clustering_coefficient >= seuil2:
        return True
    else:
        return False

# Calcul du degré d'un nœud dans un réseau
def node_degree(network, node):
    degree = 0
    for interaction in network:
        if node in interaction:
            degree += 1
    return degree

# Lecture des protéines à partir du fichier 'prot.txt'
file_name_prot = '/home/aymen/.config/spyder-py3/prot.txt'
proteins = read_proteins(file_name_prot)

# Paramètres pour la génération aléatoire du réseau
num_interactions = 10  # Nombre d'interactions à générer

# Génération aléatoire du réseau à partir des protéines lues
random_network = generate_random_network(proteins, num_interactions)

# Écriture des données du réseau dans le fichier 'proteines.txt'
file_name_network = '/home/aymen/Bureau/prot.txt'
write_network_data(file_name_network, random_network)

# Lecture des données du fichier 'proteines.txt'
network_data = read_network_data(file_name_network)

# Convertir le réseau en format de graphe pour les fonctions d'analyse de réseau
graph = {node: [] for node in set(sum(random_network, ()))}
for interaction in random_network:
    node1, node2 = interaction
    weight = 1  # Pour un réseau non pondéré, nous attribuons unerandom_network pondération arbitraire de 1
    graph[node1].append((node2, weight))
    graph[node2].append((node1, weight))

# Calcul des analyses du réseau
characteristic_distance = average_shortest_path_length(graph)
small_world = is_small_world(graph)


# Affichage des résultats
print("Network:", random_network)
print("Characteristic distance:", characteristic_distance)
if small_world:
    print("Le réseau est de type Small World.")
else:
    print("Le réseau n'est pas de type Small World.")

# Calcul du degré d'un nœud
node = input("saisir le nom de noeud : ") # Nœud pour lequel vous souhaitez calculer le degré
degree = node_degree(random_network , node)
print(f"Degré du nœud {node}:", degree)
