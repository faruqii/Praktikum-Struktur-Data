from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
        self.distance = {}

    def add_graph(self,cities):
        if cities in self.graph:
            return "City already exists"
        else:
            self.graph[cities] = []
            self.distance[cities] = []
            return f'{cities} added to graph'

    def add_distance(self, fromCity, toCity, distance:int):
        self.graph[fromCity].append(toCity)
        self.graph[toCity].append(fromCity)
        self.distance[(fromCity,toCity)] = distance
        self.distance[(toCity,fromCity)] = distance

    def deleteGraph(self, cities):
        if cities in self.graph:
            del self.graph[cities]
            return f'{cities} deleted from graph'
        else:
            return f'{cities} not found in graph'

    def printGraph(self):
        for key, value in self.graph.items():
            print(key, value)

class Main:
    def __init__(self):
        self.g = Graph()

    def countDistance(self,start,end):
        if start not in self.g.graph or end not in self.g.graph:
            return "Invalid City"
        if start == end:
            return 0
        visited = set()
        queue = [(start,0)]
        while queue:
            node,weight = queue.pop(0)
            visited.add(node)
            for next_node in self.g.graph[node]:
                if next_node == end:
                    return weight + self.g.distance[(node,next_node)]
                if next_node not in visited:
                    queue.append((next_node,weight + self.g.distance[(node,next_node)]))
        return "Route Not Possible"


    def dijkstra(self,start,end):
        shortest_distance = {start :(None,0)}
        current_node = start
        visited = set()

        while current_node != end:
            visited.add(current_node)
            destinations = self.g.graph[current_node]
            weight_to_current_node = shortest_distance[current_node][1]

            for next_node in destinations:
                weight = self.g.distance[(current_node,next_node)] + weight_to_current_node
                if next_node not in shortest_distance:
                    shortest_distance[next_node] = (current_node,weight)
                else:
                    current_shortest_weight = shortest_distance[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_distance[next_node] = (current_node,weight)

            next_destinations = {node: shortest_distance[node] for node in shortest_distance if node not in visited}
            if not next_destinations:
                return "Route Not Possible"
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_distance[current_node][0]
            current_node = next_node
        path = path[::-1]
        return path

    def main(self):
        print("1.Add City")
        print("2.Add Distance")
        print("3.Find Shortest Path")
        print("4.Print City")
        print("5.Delete City")
        print("6.Exit")
        choice = int(input("Enter your choice: "))
        while True:
            if choice == 1:
                cities = input("Enter cities: ")
                print(self.g.add_graph(cities))
            elif choice == 2:
                city1,city2, distance = input("Enter distance from,to,distance : ").split(",")
                self.g.add_distance(city1,city2,int(distance))
            elif choice == 3:
                city1,city2= input("Enter Route From-To: ").split(",")
                print(f'The Route is {self.dijkstra(city1,city2)} with distance {self.countDistance(city1,city2)} KM')
            elif choice == 4:
                print(self.g.printGraph())
            elif choice == 5:
                cities = input("Enter city name to delete: ")
                print(self.g.deleteGraph(cities))
            elif choice == 6:
                print("Thank you")
                break
            else:
                print("Invalid Choice")
            choice = int(input("\nEnter your choice: "))
            
class User:
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setPassword(self, password):
        self.password = password

    def getPassword(self):
        return self.password
    
    def setCompanyName(self, companyName):
        self.companyName = companyName

    def getCompanyName(self):
        return self.companyName

    def displayInfo(self):
        print(f"Name: {self.name} Work At {self.companyName}")
        
if __name__ == "__main__":
    m = Main()
    user = User()
    print('Welcome to Google Maps')
    print('1.Login')
    print('2.Exit')
    while True:
        choice = int(input('Enter your choice: '))
        if choice == 1:
            name = input('Enter your name: ')
            password = input('Enter your password: ')
            user.setName(name)
            user.setPassword(password)
            if password == user.getPassword():
                print('\nLogin Successful')
                print(f'\nWelcome {user.getName()} to Google Maps')
                companyName = input('Enter your company name: ')
                user.setCompanyName(companyName)
                print("1.Use Service")
                print("2.Display User Info")
                menu = int(input('Enter your choice: '))
                if menu == 1:
                    print()
                    print(f"Welcome to the {user.getCompanyName()} Logistic Service")
                    m.main()
                elif menu == 2:
                    user.displayInfo()
                    break
        elif choice == 2:
            print('Thank you for using Google Maps')
            break
        else:
            print('Invalid Choice')