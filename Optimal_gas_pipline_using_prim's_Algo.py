import networkx as nx
import matplotlib.pyplot as plt

def prim(graph):
    min_spanning_tree = nx.minimum_spanning_tree(graph)
    return min_spanning_tree

def visualize_gas_pipelines(graph, min_spanning_tree):
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_color='lightblue', font_size=8)
    plt.title('Original Gas Pipeline Network')

    # minimum spanning tree
    plt.subplot(1, 2, 2)
    nx.draw(min_spanning_tree, pos, with_labels=True, font_weight='bold', node_color='lightgreen', font_size=8)
    plt.title('Optimized Gas Pipeline Network (Minimum Spanning Tree)')

    plt.tight_layout()
    plt.show()

G = nx.complete_graph(5)
for edge in G.edges():
    G.edges[edge]['weight'] = 1

minimum_spanning_tree = prim(G)
visualize_gas_pipelines(G, minimum_spanning_tree)
