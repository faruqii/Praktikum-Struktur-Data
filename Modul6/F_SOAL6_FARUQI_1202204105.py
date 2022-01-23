import pandas as pd
from time import time

runtime = time()

class Search:

    # Constructor
    def __init__(self,key: str):
        self.key = key 

    def readFile(self,filename: str):
        # Read file using pandas and convert to list
        file = pd.read_csv(filename)
        file = file.values.tolist()
        return file

    def sort(self,file):
        # Sort whole file using Selection Sort 
        for i in range(len(file)):
            min_index = i
            for j in range(i + 1, len(file)):
                if file[min_index][1].upper() > file[j][1].upper(): # i use .upper() to make sure the comparison is case insensitive
                    min_index = j
            file[i], file[min_index] = file[min_index], file[i] # Swap the value
        
        return file # Return the result file
    
    def InterpolationSearch(self,file: list):
        # Interpolation Search is develop from binary search
        # the algorithm is the same as binary search, but the search range is not fixed
        # the search range is determined by the key
        # not like binary search data is divided into two parts, the search range is determined by the key
        # Since InterpolationSearch can't handle String, i usse this index to handle it
        idx = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']
        low = 0
        high = len(file) - 1
        point = 0
        # loop through the whole file
        while (low <= high and self.key >= file[low][1] and self.key <= file[high][1]):
            # Calculate the point
            if (low == high):
                if file[low][1] == self.key :
                    point = 1
                    return low
                else:
                    return -1

            # Position of the point is determined by this formula 
            position = low + int(((float(high-low) // (idx.index(file[high][1][0]) - idx.index(file[low][1][0]))) * (idx.index(self.key[0]) - idx.index(file[low][1][0] ))))
            # Check if the point is in the range
            if file[position][1] == self.key :
                point = 1
                return position # Return the position
            if file[position][1] < self.key :
                low = position + 1 # Move the low point to the position
            else:
                high = position - 1 # Move the high point to the position
        # If the point is not found, return -1
        if (point == 0):
            return - 1  
        # Thiis Algorithm is not efficient yet, because the search can't find whole key in the file 
        # for example if the key is 'arXiv Mesoscale and Nanoscale Physics (cond-mat.mes-hall)' it will return -1
        # but it easy to understand, it can be improved by using the formula to calculate the point

if __name__ == '__main__':     

    search = input("Enter the key to search: ")
    obj = Search(search)
    
    file = obj.readFile('Daspro.csv')
    file = obj.sort(file)
    result = obj.InterpolationSearch(file)

    if result == -1:
        print(f"{search} not found in the data")
    else:        
        print(file[int(result)])  # Print the result using index
    
    print(f"Runtime: {time() - runtime}")
