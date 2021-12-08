class Graph():
    def __init__(self):
        self.graph = {}
        self.vertices = 0
        self.visited = []
        self.distance = 0

    def addGraph(self, vertex):
        if vertex in self.graph:
            print("Kota sudah diinput")
        else:
            self.graph[vertex]={}
            self.vertices += 1

    def addEdge(self, vertex1, vertex2, edge):
        if vertex1 not in self.graph:
            print("Kota ", vertex1, " tidak ada di data")
        elif vertex2 not in self.graph:
            print("Kota ", vertex2, " tidak ada di data")
        else:
            self.graph[vertex1][vertex2] = []
            self.graph[vertex1][vertex2].append(edge)

            self.graph[vertex2][vertex1] = []
            self.graph[vertex2][vertex1].append(edge)

    def cobaprint(self):
        return self.graph

    def destination(self, start, end):
        # self.visited.append(start)
        if start == end:
            print("Kota yang dituju sama saja")
        elif start not in self.graph:
            print("Kota tidak ada di data")
        elif end not in self.graph:
            print("Kota tidak ada di data")
        else:
            if end in self.graph[start]:
                if start in self.visited:
                    self.visited.append(end)
                else:
                    self.visited.append(start)
                    self.visited.append(end)
                for i in self.graph[start][end]:
                    self.distance += i
                print("The route is ", self.visited, "with the distance ", self.distance)

            else:
                llist=[]
                city = []
                if start in self.visited:
                    pass
                else:
                    self.visited.append(start)

                for i in self.graph[start]:
                    city.append(i)
                    for j in self.graph[start][i]:
                        llist.append(j)

                self.distance += min(llist)             
                temu = llist.index(min(llist))
                self.visited.append(city[temu])
                return self.destination(city[temu], end)
                
coba = Graph()
coba.addGraph("Bojongsoang")
coba.addGraph("Arcamanik")
coba.addGraph("Dago")
coba.addGraph("Ciumbuleuit")

coba.addEdge("Bojongsoang", "Arcamanik", 70)
coba.addEdge("Bojongsoang", "Dago", 150)
coba.addEdge("Bojongsoang", "Ciumbuleuit", 100)
coba.addEdge("Arcamanik", "Ciumbuleuit", 90)
coba.addEdge("Dago", "Ciumbuleuit", 110)

coba.destination("Arcamanik", "Dago")