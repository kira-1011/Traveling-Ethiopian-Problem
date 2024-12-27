# Traveling Ethiopian Problem

A Python implementation of uninformed and informed(Dijkstra's) search strategies to solve the traveling Ethiopian problem. This project simulates an AI agent that plans tours across Ethiopia using different search strategies.

## Problem Statement

Ethiopia, known for its rich cultural heritage and diverse geography, has numerous cities connected by road networks. The program implements an AI agent that plans a tour across Ethiopia, starting from a designated city and visiting other cities based on specific constraints. The agent implements uninformed search strategies to find paths under different conditions.

## Assumptions

- The agent is given a starting city and a goal city
- The agent is given a list of cities to visit
- The agent is given a list of roads between cities
- The agent is given a list of distances between cities

## Graph Representation

- Cities are represented as nodes
- Roads between cities are edges
- The graph is undirected with varying distances (costs)
- Distances are in kilometers

## Features

- **Multiple Search Algorithms:**

  - Depth First Search (DFS) - finds any feasible path
  - Breadth First Search (BFS) - finds path with minimum number of cities
  - Weighted BFS - finds shortest path by distance

- **Interactive Console Menu**
- **Graph Visualization** using NetworkX
- **Real Ethiopian Cities** with approximate road distances

## Requirements

run `pip install -r requirements.txt` to install the dependencies

## How to run

run `python main.py` to start the program
