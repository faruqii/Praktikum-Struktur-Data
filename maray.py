class Graph:

    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def add_graph_node(self, node):
        if node not in self.__graph_dict:
            self.__graph_dict[node] = []

    def add_distance(self, start_node, end_node, distance):
        self.__graph_dict[start_node].append((end_node, distance))

    def depth_first_search(self, start_node):
        visited = []
        stack = [start_node]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                stack.extend(self.__graph_dict[node])
        return visited
    
    def print_graph(self):
        for node in self.__graph_dict:
            print(node, ":", self.__graph_dict[node])

if __name__ == '__main__':
    graph = Graph()
    while True:
        print('''
        1. Add Cities
        2. Add City distance
        3. Get Distance from City to City
        4. Print Cities
        ''')
        choice = int(input("Enter your choice: "))
        if choice == 1:
            city = input("Enter city name: ")
            graph.add_graph_node(city)
        elif choice == 2:
            city1 = input("Enter city name: ")
            city2 = input("Enter city name: ")
            distance = int(input("Enter distance: "))
            graph.add_distance(city1, city2,distance)
        elif choice == 3:
            city1 = input("Enter city name: ")
            city2 = input("Enter city name: ")
            distance_city = print(graph.depth_first_search(city1))
            print(f"Distance from {city1} to {city2} is {distance_city}")
        elif choice == 4:
            graph.print_graph()
        else:
            print("Invalid choice")
            break