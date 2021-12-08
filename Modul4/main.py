class Graph:

    def __init__(self):
        self.graph = {}

    def add_cities(self, cities):
        for city in cities:
            self.add_edge(city, city, 0)

    def add_edge(self, city1, city2, distance: int):
        if city1 not in self.graph:
            self.graph[city1] = [[city2, distance]]
        else:
            self.graph[city1].append([city2, distance])

    def get_cities(self):
        for cities in self.graph:
            print(f'City {cities} : {self.graph[cities]}')

    
    def get_path_between_city(self, cities, city1, city2, path=[]):
        path = path + [city1]
        if city1 == city2:
            return path
        if city1 not in cities:
            return None
        for city_connected, distance_connected in self.graph[city1]:
            if city_connected not in path:
                newpath = self.get_path_between_city(cities, city_connected, city2, path)
                if newpath: 
                    return newpath
        return None 

    def get_shorthest_path(self, city1, city2):
        if city1 not in self.graph:
            return "City not found"
        if city2 not in self.graph:
            return "City not found"
        if city1 == city2:
            return 0
        visited = set()
        queue = [(city1, 0)]
        while len(queue) > 0:
            city, distance = queue.pop(0)
            visited.add(city)
            if city == city2: 
                return distance
            for city_connected, distance_connected in self.graph[city]:
                if city_connected not in visited:
                    queue.append((city_connected, distance + distance_connected))

if __name__ == '__main__':
    app = Graph()
    print('Welcome to the city distance calculator!')
    print("1. Add cities")
    print("2. Add distance between cities")
    print("3. Get distance between cities")
    print("4. Print cities")
    print("5. Exit")
    while True:
        menu = int(input('Enter your choice: '))
        if menu == 1:
            cities = input('Enter the cities: ').split(',')
            app.add_cities(cities)
        elif menu == 2:
            city1, city2, distance = input('Enter the cities and distance: ').split(',')
            app.add_edge(city1, city2, int(distance))
        elif menu == 3:
            city1, city2 = input('Enter the cities: ').split(',')
            route = app.get_path_between_city(app.graph,city1, city2)
            distanceCount = app.get_shorthest_path(city1, city2)
            print(f'Rutenya adalah {route} dengan jarak tempuh {distanceCount} km') 
        elif menu == 4:
            print(app.get_cities())
        elif menu == 5:
            break

    