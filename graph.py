import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

closedRoad = 9999999999

class Graph:
    def __init__(self, size: int) -> None:
        self.size = size
        self.solution = 0
        self.array = np.zeros((self.size, self.size))

    def read_graph(self, filename: str) -> None:
        self.array = np.loadtxt(filename, dtype=int)
        self.size = self.array.shape[0]

    def save_graph(self) -> None:
        np.savetxt(f"datasets/{self.size}.txt", self.array, fmt='%d')

    def print_graph(self) -> None:
        if (self.solution > 0):
            print (self.solution)
        print(self.array)

    def display_graph(self):
        G = nx.Graph()
        for i in range (0, self.size):
            G.add_node(i, pos=(random.randint(0,self.size),random.randint(0,self.size)))
        for i in range (0, self.size):
            for j in range (0, i):
                if ( self.array[i][j] != 0):
                    G.add_edge(i, j, weight = self.array[i][j])
        pos = nx.get_node_attributes(G,'pos')
        nx.draw(G,pos)
        labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G,pos, edge_labels=labels)
        plt.show()

    def get_fitness(self, route):
        fitness = 0
        for i in range(0, len(route)-1):
            temp = self.array[route[i]-1][route[i+1]-1]
            if (temp == 0):
                temp = closedRoad
            fitness = fitness + temp
        return 1/fitness

    def route_length(self,route):
        length = 0
        for i in range(0, len(route)-1):
            temp = self.array[route[i]-1][route[i+1]-1]
            length = length + temp
        return length
    
if __name__ == "__main__":
    graph = Graph(5)
    print(graph.array)
    graph.read_graph("datasets/5.txt")
    print(graph.array)
    graph.display_graph()