import networkx as nx
import matplotlib.pyplot as plt

def warshall_algorithm(graph):
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = graph[i][j] or (graph[i][k] and graph[k][j])
    return graph

def is_connected(graph, start, end):
    return graph[start][end] == 1

def visualize_graph(graph, title="Graph"):
    G = nx.DiGraph()
    n = len(graph)
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                G.add_edge(i, j)
    
    plt.figure(figsize=(6, 6))
    nx.draw(G, with_labels=True, node_color='skyblue', font_weight='bold', node_size=700, arrowstyle='->', arrowsize=20)
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    graph = [
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0]]

    print("Original Flight Connections Matrix:")
    for row in graph:
        print(row)

    visualize_graph(graph, title="Original Flight Connections")    
    closure = warshall_algorithm(graph)

    print("\nTransitive Closure Matrix:")
    for row in closure:
        print(row)

    visualize_graph(closure, title="Transitive Closure (All Reachable Routes)")

    try:
        start = int(input("Enter Start Point (node index): "))
        end = int(input("Enter End Point (node index): "))
        if start < 0 or end < 0 or start >= len(graph) or end >= len(graph):
            print("Invalid node indices. Please enter indices within range.")
        else:
            if is_connected(closure, start, end):
                print(f"\nThere is a route from Airport {start} to Airport {end}.")
            else:
                print(f"\nNo route exists from Airport {start} to Airport {end}.")
    except ValueError:
        print("Invalid input. Please enter integer indices.")