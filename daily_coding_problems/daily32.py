"""
Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantities.

Solution:
Need to find the 'shortest path' between nodes which are different currencies
Nodes are represented by different rows and columns and the values are the exchange rate between each currency
Looking for a negative cycle where the sum of the path is <0
In this case rather than getting rate1 * rate2 * ... > 1 (which would give us a greater total than our starting out cash)
Also log(a * b) = log(a) + log(b)
So -log(rate1) - log(rate2) - .... < 0 is an indicator of a negative cycle

Use Bellman-Ford algorithm for shortest path
Need to iterate V-1 number of times (V is number of nodes) and update all the edges with each iteration


"""
from math import log

def print_matrix(matrix):
    for row in matrix:
        print (row)

def solution(rates, currencies):
    log_matrix = [[-log(x) for x in row] for row in rates]
    # dist_matrix = [[float('inf') for x in row] for row in rates]
    n = len(rates)

    # for x in range(n):
    #     dist_matrix[x][x] = 0
    # print (print_matrix(dist_matrix))
    # print (print_matrix(log_matrix))

    min_dist = [float('inf')] * n
    min_dist[0] = 0

    pre = [-1] * n

    for _ in range(10):
        # print(min_dist)
        for x in range(n): #x row
            for y in range(n): #y column
                # if x != y:
                if min_dist[y] > min_dist[x] + log_matrix[x][y]:
                    min_dist[y] = min_dist[x] + log_matrix[x][y]
                    pre[y] = x
                    # if dist_matrix[x][y] > dist_matrix[x][x] + log_matrix[x][y]:
                    #     dist_matrix[x][y] = dist_matrix[x][x] + log_matrix[x][y]

    # If we can still relax edges, then we have a negative cycle
    for v in range(n):
        for w in range(n):
            if min_dist[w] > min_dist[v] + log_matrix[v][w]:
                print_cycle = [w,v]
                # print (min_dist)
                # return True
                while pre[v] not in print_cycle:
                    print_cycle.append(pre[v])
                    v = pre[v]
                print_cycle.append(pre[v])
                print(" --> ".join([currencies[p] for p in print_cycle[::-1]]))

    print (min_dist)
    return False
    # print (print_matrix(dist_matrix))



# def test():
#     solution()

rates = [
  # 'PLN',   'EUR',   'USD',   'RUB',   'INR',   'MXN'
    [1,      0.23,    0.25,    16.43,   18.21,   4.94],  #'PLN'
    [4.34,     1,     1.11,    71.40,   79.09,   21.44], #'EUR'
    [3.93,   0.90,      1,     64.52,   71.48,   19.37], #'USD'  0.9Eur = 1USD
    [0.061,  0.014,   0.015,     1,      1.11,    0.30], #'RUB'
    [0.055,  0.013,   0.014,    0.90,      1,     0.27], #'INR'
    [0.20,   0.047,   0.052,    3.33,    3.69,      1],  #'MXN'
]

currencies = ('PLN', 'EUR', 'USD', 'RUB', 'INR', 'MXN')

# rates = [
#   # 'PLN',   'EUR', 'USD'
#     [1,      0.23, 0.25],  #'PLN'
#     [4.34,     1,  1.11], #'EUR'
#     [3.93,   0.90,    1]#'USD'
# ]
# currencies = ('PLN', 'EUR')

print(solution(rates, currencies))


# from typing import Tuple, List
# from math import log
#
# rates = [
#     [1, 0.23, 0.25, 16.43, 18.21, 4.94],
#     [4.34, 1, 1.11, 71.40, 79.09, 21.44],
#     [3.93, 0.90, 1, 64.52, 71.48, 19.37],
#     [0.061, 0.014, 0.015, 1, 1.11, 0.30],
#     [0.055, 0.013, 0.014, 0.90, 1, 0.27],
#     [0.20, 0.047, 0.052, 3.33, 3.69, 1],
# ]
#
# currencies = ('PLN', 'EUR', 'USD', 'RUB', 'INR', 'MXN')
#
#
# def negate_logarithm_convertor(graph: Tuple[Tuple[float]]) -> List[List[float]]:
#     ''' log of each rate in graph and negate it'''
#     result = [[-log(edge) for edge in row] for row in graph]
#     return result
#
#
# def arbitrage(currency_tuple: tuple, rates_matrix: Tuple[Tuple[float, ...]]):
#     ''' Calculates arbitrage situations and prints out the details of this calculations'''
#
#     trans_graph = negate_logarithm_convertor(rates_matrix)
#
#     # Pick any source vertex -- we can run Bellman-Ford from any vertex and get the right result
#
#     source = 0
#     n = len(trans_graph)
#     min_dist = [float('inf')] * n
#
#     pre = [-1] * n
#
#     min_dist[source] = source
#
#     # 'Relax edges |V-1| times'
#     for _ in range(n-1):
#         for source_curr in range(n):
#             for dest_curr in range(n):
#                 if min_dist[dest_curr] > min_dist[source_curr] + trans_graph[source_curr][dest_curr]:
#                     min_dist[dest_curr] = min_dist[source_curr] + trans_graph[source_curr][dest_curr]
#                     pre[dest_curr] = source_curr
#
#     # if we can still relax edges, then we have a negative cycle
#     for source_curr in range(n):
#         for dest_curr in range(n):
#             if min_dist[dest_curr] > min_dist[source_curr] + trans_graph[source_curr][dest_curr]:
#                 # negative cycle exists, and use the predecessor chain to print the cycle
#                 print_cycle = [dest_curr, source_curr]
#                 # Start from the source and go backwards until you see the source vertex again or any vertex that already exists in print_cycle array
#                 while pre[source_curr] not in  print_cycle:
#                     print_cycle.append(pre[source_curr])
#                     source_curr = pre[source_curr]
#                 print_cycle.append(pre[source_curr])
#                 print("Arbitrage Opportunity: \n")
#                 print(" --> ".join([currencies[p] for p in print_cycle[::-1]]))
#
#
# if __name__ == "__main__":
#     arbitrage(currencies, rates)

# Time Complexity: O(N^3)
# Space Complexity: O(N^2)

'''
node example
'''

# from collections import defaultdict
#
# # Class to represent a graph
# class Graph:
#
#     def __init__(self, vertices):
#         self.V = vertices # No. of vertices
#         self.graph = [] # default dictionary to store graph
#
#     # function to add an edge to graph
#     def addEdge(self, u, v, w):
#         self.graph.append([u, v, w])
#
#     # utility function used to print the solution
#     def printArr(self, dist):
#         print("Vertex   Distance from Source")
#         for i in range(self.V):
#             print("% d \t\t % d" % (i, dist[i]))
#
#     # The main function that finds shortest distances from src to
#     # all other vertices using Bellman-Ford algorithm.  The function
#     # also detects negative weight cycle
#     def BellmanFord(self, src):
#
#         # Step 1: Initialize distances from src to all other vertices
#         # as INFINITE
#         dist = [float("Inf")] * self.V
#         dist[src] = 0
#
#
#         # Step 2: Relax all edges |V| - 1 times. A simple shortest
#         # path from src to any other vertex can have at-most |V| - 1
#         # edges
#         for i in range(self.V - 1):
#             # Update dist value and parent index of the adjacent vertices of
#             # the picked vertex. Consider only those vertices which are still in
#             # queue
#             for u, v, w in self.graph:
#                 if dist[u] != float("Inf") and dist[u] + w < dist[v]:
#                         dist[v] = dist[u] + w
#
#         # Step 3: check for negative-weight cycles.  The above step
#         # guarantees shortest distances if graph doesn't contain
#         # negative weight cycle.  If we get a shorter path, then there
#         # is a cycle.
#
#         for u, v, w in self.graph:
#                 if dist[u] != float("Inf") and dist[u] + w < dist[v]:
#                         print ("Graph contains negative weight cycle")
#                         return
#
#         # print all distance
#         self.printArr(dist)
#
# g = Graph(5)
# g.addEdge(0, 1, -1)
# g.addEdge(0, 2, 4)
# g.addEdge(1, 2, 3)
# g.addEdge(1, 3, 2)
# g.addEdge(1, 4, 2)
# g.addEdge(3, 2, 5)
# g.addEdge(3, 1, 1)
# g.addEdge(4, 3, -3)
#
# # Print the solution
# g.BellmanFord(0)
