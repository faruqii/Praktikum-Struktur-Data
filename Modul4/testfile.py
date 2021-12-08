class Graph:
    def __init__(self):
        self.graph = {}
        self.vertices_no = 0

    def insertVertex(self, vertex):
        if vertex in self.graph:
            print("Kota sudah ada")
        else:
            self.graph[vertex]={}
            self.vertices_no+=1
            print(f"kota {vertex} berhasil ditambahkan! \n")

    def insertEdge(self,vertex1,vertex2,jarak):
        if vertex1 not in self.graph:
            print(f"Kota {vertex1} belum di input")
        elif vertex2 not in self.graph:
            print(f"Kota {vertex2} belum di input")
        else:
            self.graph[vertex1][vertex2] = jarak
            self.graph[vertex2][vertex1] = jarak
            print("Jarak berhasil ditambahkan\n")

    def getGraph(self):
        for vertex in self.graph:
            print(vertex,self.graph[vertex])

    def deptFirstSearch(self,start,end):
        jarak = 0
        queue = [start]
        visited = set()
        print("Rute = ",end="")
        while len(queue)>0:
            current = queue.pop()
            if current != end:
                print(current,end=" - ")
                visited.add(current)
                for i in self.graph[current]:
                    if i not in visited:
                        if i in queue:
                            queue.remove(i)
                        queue.append(i)
                jarak += self.graph[current][i]
            else:
                print(current)
                visited.add(current)
                for i in self.graph[current]:
                    if i not in visited:
                        if i in queue:
                            queue.remove(i)
                        queue.append(i)
                break

        print(f"jarak = {jarak} km")

if __name__ == '__main__':
    g=Graph()
    while True:
        print("1. Insert Vertex")
        print("2. Insert Edge")
        print("3. Get Graph")
        print("4. Depth First Search")
        print("5. Exit")
        choice = int(input("Masukkan pilihan anda: "))
        if choice == 1:
            vertex = input("Masukkan kota: ")
            g.insertVertex(vertex)
        elif choice == 2:
            vertex1 = input("Masukkan kota awal: ")
            vertex2 = input("Masukkan kota akhir: ")
            jarak = int(input("Masukkan jarak: "))
            g.insertEdge(vertex1,vertex2,jarak)
        elif choice == 3:
            g.getGraph()
        elif choice == 4:
            start = input("Masukkan kota awal: ")
            end = input("Masukkan kota akhir: ")
            g.deptFirstSearch(start,end)
        elif choice == 5:
            break
        else:
            print("Pilihan tidak ada")
            
    # g.insertVertex("Arcamanik")
    # g.insertVertex("Bojongsoang")
    # g.insertVertex("Ciumbuleuit")
    # g.insertVertex("Dago")

    # g.insertEdge("Arcamanik", "Bojongsoang", 70)
    # g.insertEdge("Arcamanik", "Ciumbuleuit", 90)
    # g.insertEdge("Bojongsoang", "Ciumbuleuit", 100)
    # g.insertEdge("Bojongsoang", "Dago", 150)
    # g.insertEdge("Ciumbuleuit", "Dago", 110)

    # g.getGraph()
    # g.deptFirstSearch("Arcamanik", "Dago")
