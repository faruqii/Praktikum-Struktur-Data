import heapq

class vertex:
    def __init__(self,nodes):
        self.id = nodes
        self.adjacent = {}
        self.distance = 0
        self.visited = False
        self.previous = None

    def add_neighbor(self,neighbor,weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self,neighbor):
        return self.adjacent[neighbor]

    def set_distance(self,d):
        self.distance = d

    def get_distance(self):
        return self.distance

    def set_previous(self,prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self,node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self,n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self,frm,to,cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self,current):
        self.previous = current

    def get_previous(self,current):
        return self.previous

class Main:
    def __init__(self):
        self.graph = Graph()

    def shortest(self,v,path):
        if v.previous:
            path.append(v.previous.get_id())
            self.shortest(v.previous, path)
        return

    def dijkstra(self,graph,start):
        start.set_distance(0)
        unvisited_queue = [x for x in graph]
        while len(unvisited_queue):
            current = unvisited_queue.pop(0)
            for next in current.adjacent:
                if next.visited:
                    continue
                new_dist = current.get_distance() + current.get_weight(next)
                if new_dist < next.get_distance():
                    next.set_distance(new_dist)
                    next.set_previous(current)
                    unvisited_queue.append(next)
            current.set_visited()

        while len(unvisited_queue):
            unvisited_queue.pop()
        unvisited_queue = [(v.get_distance(),v) for v in graph if v.get_distance() != 0]
        heapq.heapify(unvisited_queue) 

if __name__ == '__main__':
    g = Graph()
    print('Welcome to the city distance calculator!')
    print("1. Add cities")
    print("2. Add distance between cities")
    print("3. Get distance between cities")
    print("4. Print cities")
    print("5. Exit")
    while True:
        
        print("\nChoose an option:")
        choice = input()
        if choice == '1':
            print("Enter the name of the city:")
            name = input()
            g.add_vertex(name)
        elif choice == '2':
            print("Enter the name of the city:")
            name = input()
            print("Enter the name of the city:")
            name2 = input()
            print("Enter the distance between the two cities:")
            distance = input()
            g.add_edge(name,name2,distance)
        elif choice == '3':
            print("Enter the name of the city:")
            name = input()
            print("Enter the name of the city:")
            name2 = input()
            print("The distance between the two cities is:")
            print(g.get_vertex(name).get_weight(g.get_vertex(name2)))
        elif choice == '4':
            print("The cities are:")
            for i in g:
                print(i.get_id())
        elif choice == '5':
            break
        else:
            print("Invalid input")


    