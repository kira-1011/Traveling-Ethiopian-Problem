from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

'''
Problem Statement:
Ethiopia, known for its rich cultural heritage and diverse geography, has numerous cities connected by road networks. You are tasked to develop an AI agent that plans a tour across Ethiopia, starting from a designated city and visiting other cities based on specific constraints. The agent should implement uninformed search strategies to find paths under different conditions.

Graph Representation:
The cities are represented as nodes, and roads between them are edges. The graph is undirected and may include varying distances (costs). You will be provided the following:

City Data:

cities: A list of city names.
roads: A dictionary where each key is a city, and the value is a list of tuples (connected_city, distance).

Input:
cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}
'''

cities = ['Addis Ababa', 'Bahir Dar', 'Gondar',
          'Hawassa', 'Mekelle', 'Adama', 'Dilla', 'Dire Dawa']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275), ('Adama', 99)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300), ('Hawassa', 200)],
    'Hawassa': [('Addis Ababa', 275), ('Dilla', 90), ('Gondar', 200)],
    'Mekelle': [('Gondar', 300)],
    'Adama': [('Addis Ababa', 99), ('Dire Dawa', 400)],
    'Dilla': [('Hawassa', 90)],
    'Dire Dawa': [('Adama', 400)]
}


def dfs(graph, node, goal, visited):

    visited.add(node)

    # if reached goal return the path
    if node == goal:
        return [node]

    # visit neighbours
    for nbr, cost in graph[node]:
        if nbr not in visited:
            path = dfs(graph, nbr, goal, visited)

            # if path to goal state found
            if path:
                return [node] + path

    return []


def bfs(graph, node, goal):

    queue = deque([node])
    parent_map = {}
    visited = set([])

    while queue:
        curr_node = queue.popleft()
        visited.add(curr_node)

        if curr_node == goal:
            path = []
            parent = curr_node

            # construct path
            while parent:
                path.append(parent)
                parent = parent_map.get(parent, None)

            return path

        for nbr, cost in graph[curr_node]:
            if nbr not in visited:
                parent_map[nbr] = curr_node
                queue.append(nbr)


def weighted_bfs(graph, start, goal):

    queue = deque([start])
    path = {key: (start, float('inf')) for key in graph}
    path[start] = (start, 0)
    visited = set([])

    while queue:
        curr_node = queue.popleft()
        visited.add(curr_node)
        start_to_curr_cost = path[curr_node][1]

        for nbr, cost in graph[curr_node]:
            if nbr not in visited:
                queue.append(nbr)
                curr_to_nbr_cost = cost
                total_cost = start_to_curr_cost + curr_to_nbr_cost

                # check if there is a better minimum path to nbr node
                if total_cost < path[nbr][1]:
                    path[nbr] = (curr_node, total_cost)

    # construct path and total cost
    total_cost = path[goal][1]
    parent = goal
    final_path = []

    print(path)
    while parent != start:
        final_path.append(parent)
        parent = path[parent][0]

    final_path.append(start)
    final_path.reverse()
    return (final_path, total_cost)


def draw_graph_with_path(start, goal, path):
    G = nx.Graph()
    for city, connections in roads.items():
        for connected_city, distance in connections:
            G.add_edge(city, connected_city, weight=distance)
    plt.figure(figsize=(15, 10))
    pos = nx.kamada_kawai_layout(G)
    # Draw all edges first in black
    nx.draw_networkx_edges(G, pos, width=1, edge_color='black')
    # Draw path edges in red and thicker
    path_edges = list(zip(path[:-1], path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges,
                           edge_color='red', width=3)
    # Draw all nodes
    nx.draw_networkx_nodes(G, pos, node_color='lightblue',
                           node_size=1500, linewidths=2, edgecolors='navy')
    # Highlight start node in green
    nx.draw_networkx_nodes(G, pos, nodelist=[
                           start], node_color='green', node_size=1500, linewidths=2, edgecolors='darkgreen')
    # Highlight goal node in yellow
    nx.draw_networkx_nodes(G, pos, nodelist=[
                           goal], node_color='yellow', node_size=1500, linewidths=2, edgecolors='orange')
    # Add labels
    nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')
    # Add edge labels with distances
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=7)
    plt.title("Traveling Ethiopian Problem", pad=20, size=16)
    plt.axis('off')
    plt.tight_layout()
    plt.show()


def print_cities():
    print("\nAvailable Cities:")
    for i, city in enumerate(roads.keys(), 1):
        print(f"{i}. {city}")


def get_city_choice(prompt):
    while True:
        print_cities()
        try:
            choice = int(input(prompt))
            if 1 <= choice <= len(roads):
                return list(roads.keys())[choice-1]
            else:
                print("\nInvalid choice. Please select a valid number.")
        except ValueError:
            print("\nPlease enter a number.")


def print_algorithm_menu():
    print("\nSelect Algorithm:")
    print("1. Depth First Search (DFS) to find feasible path")
    print("2. Breadth First Search (BFS) to find feasible path")
    print("3. Weighted BFS to find the shortest path")


def main_menu():
    while True:
        print("\n=== Traveling Ethiopian Problem ===")

        # Get start and goal cities
        start = get_city_choice("\nSelect start city (enter number): ")
        goal = get_city_choice("Select goal city (enter number): ")

        # Get algorithm choice
        print_algorithm_menu()
        while True:
            try:
                algo_choice = int(input("\nSelect algorithm (1-3): "))
                if 1 <= algo_choice <= 3:
                    break
                print("Please select a valid option (1-3)")
            except ValueError:
                print("Please enter a number")

        # Execute chosen algorithm
        if algo_choice == 1:
            path = dfs(roads, start, goal, set())
            print(f"\nDFS Path: {' -> '.join(path)}")
            draw_graph_with_path(start, goal, path)

        elif algo_choice == 2:
            path = bfs(roads, start, goal)
            print(f"\nBFS Path: {' -> '.join(path)}")
            draw_graph_with_path(start, goal, path)

        elif algo_choice == 3:
            path, cost = weighted_bfs(roads, start, goal)
            print(f"\nWeighted BFS Path: {' -> '.join(path)}")
            print(f"Total Distance: {cost} km")
            draw_graph_with_path(start, goal, path)

        # Ask if user wants to continue
        while True:
            again = input("\nTry another path? (y/n): ").lower()
            if again in ['y', 'n']:
                break
            print("Please enter 'y' or 'n'")

        if again == 'n':
            print("\nThank you for using Ethiopian Cities Pathfinding!")
            break


if __name__ == "__main__":
    main_menu()
