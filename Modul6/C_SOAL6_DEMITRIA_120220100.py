import pandas as pd
import time

exc = time.time()

class Searching:
    def __init__(self, dataset, type):
        self.dataset = dataset
        self.type = type

    def sort(self):
        self.data = pd.read_csv(self.dataset)
        self.data = self.data.values.tolist()

        for i in range(len(self.data)):
            for j in range(len(self.data) - i - 1):
                if self.data[j][self.type] > self.data[j+1][self.type]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]

        return self.column()

    def column(self):
        if self.type == 0:
            key = input("\nEnter the Rank: ")
            print(self.binarySearch(int(key)))

        elif self.type == 1:
            key = input("\nEnter the Publication: ")
            for dt in self.data:
                if key in dt[1]:
                    print(self.binarySearch(dt[1]))

        elif self.type == 2:
            key = input("\nEnter the H5 - Index: ")
            for dt in self.data:
                if dt[2] == int(key):
                    print(dt);self.binarySearch(int(dt[2]))

        elif self.type == 3:
            key = input("\nEnter the H5 - Median: ")
            for dt in self.data:
                if dt[3] == int(key):
                    print(dt);self.binarySearch(int(dt[3]))

    def binarySearch(self, key):
        low = 0
        high = len(self.data) - 1

        while low <= high:
            mid = high + low // 2
            if self.data[mid][self.type] == key:
                return self.data[mid]
            elif self.data[low][self.type] == key:
                return self.data[low]
            elif self.data[high][self.type] == key:
                return self.data[high]
            elif self.data[mid][self.type] < key:
                low = mid + 1
            elif self.data[mid][self.type] > key:
                high = mid - 1

        return f"{key} not found!"

    def execution(self):
        print(f"Execution Time: {time.time() - exc} sec.")

if __name__ == '__main__':
    choice = int(input("""
        - - - Menu - - -
        Which column do you want to Search?
        1. Rank
        2. Publication
        3. H5 - Index
        4. H5 - Median

        Choice Menu: """))
    choice -= 1
    main = Searching("Daspro.csv", choice)
    main.sort()
    main.execution()