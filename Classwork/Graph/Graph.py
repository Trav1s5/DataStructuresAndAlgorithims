import heapq

class Graphs:
    def __init__(self,directed=False):
        self.directed = directed

        """
        graph = {
        A:(B,2) , (C,27) , (D,30)
        }
        """
        self.adj_list = dict()


    def __repr__(self):
        graph_string =" "
        for node,neighbours in self.adj_list.items():
            graph_string += f"{node} ->{neighbours}\n"
        return graph_string

    def add_node(self,node):
       if node not in self.adj_list:
           self.adj_list[node] =set()
       else:
           raise ValueError("Value already exists")

    def add_edge (self, from_node , to_node , weight =None):

        if from_node not in self.adj_list:
            self.add_node(from_node)
        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weight is None:
            # output will be: A ->  B or A - B
            self.adj_list[from_node].add(to_node)
            if not self.directed:
                self.adj_list[to_node].add(from_node)

        else:
            self.adj_list[from_node].add((to_node , weight))
            if not self.directed:
                self.adj_list[to_node].add((from_node , weight))


    def bfs(self,start_node):
        visited = set()
        queue = [start_node]
        order = []

        while queue :
            node = queue.pop( 0 )

            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)

                for neighbours in neighbours:
                    if isinstance(neighbours , tuple):
                        neighbours = neighbours[0]
                    if neighbours not in visited:
                        queue.append(neighbours)
        return order



    def dfs(self,start_node):
        visited = set()
        stack = [start_node]
        order = []

        while stack :
            node = stack.pop()

            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)

                for neighbours in sorted(neighbours , reverse=True):
                    if isinstance(neighbours , tuple):
                        neighbours = neighbours[0]
                    if neighbours not in visited:
                        stack.append(neighbours)
        return  order

    def dijkstra(self, start_node):
        distances = {node: float('inf') for node in self.adj_list}
        distances[start_node] = 0

        # Priority queue: (distance to node, node name)
        priority_queue = [(0, start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # Skip processing if a better path has already been found
            if current_distance > distances[current_node]:
                continue

            for neighbor in self.obtain_neighbours(current_node):
                if isinstance(neighbor, tuple):
                    neighbor_node, weight = neighbor
                else:
                    continue  # Skip if no weights (Dijkstra needs weighted edges)

                distance = current_distance + weight

                if distance < distances[neighbor_node]:
                    distances[neighbor_node] = distance
                    heapq.heappush(priority_queue, (distance, neighbor_node))

        return distances


    def obtain_neighbours(self , node):
        return self.adj_list.get(node, set())

if __name__ == '__main__':
    graph_obj = Graphs(directed = True)

    graph_obj.add_edge("A","B",2)
    graph_obj.add_edge("A", "J",2)
    graph_obj.add_edge("A", "C", 3)
    graph_obj.add_edge("B", "D", 4)
    graph_obj.add_edge("D", "C", 7)

    print(graph_obj)
    print("BREADTH FIRST SEARCH:\n")
    print(graph_obj.bfs("A"))
    print("DEPTH FIRST SEARCH:\n")
    print(graph_obj.dfs("A"))

    print("Dijkstra Shortest Paths from A:\n")
    print(graph_obj.dijkstra("A"))

