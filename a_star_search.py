# -*- coding: utf-8 -*-
"""A_Star_Search.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AzHxMuzSkvWwgZ5oIGnd8Y8C9zQgKAlG
"""

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


def aStarAlgo(start_node, stop_node):

    open_set = set(start_node)
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None

        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n == None:
            print("Path does not exist!")
            return None

        if n == stop_node:
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start_node)

            path.reverse()
            print("Optimal Cost:", g[m])
            return path

        open_set.remove(n)
        closed_set.add(n)
    print("Path found:", path)
    print("Path does not exist!")
    return None


def heuristic(n):
    H_dist = {"S": 7, "A": 6, "B": 2, "C": 1, "D": 0}

    return H_dist[n]


Graph_nodes = {
    "S": [("A", 1), ("B", 4)],
    "A": [("B", 2), ("C", 5), ("D", 12)],
    "B": [("C", 2)],
    "C": [("D", 3)],
}
aStarAlgo("S", "D")