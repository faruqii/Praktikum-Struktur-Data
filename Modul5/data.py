import pandas as pd

data = pd.read_csv("Data.csv")
data = data.values.tolist()

def sort(data, collumn):
    for i in range(len(data)):
        swapped = False
        for j in range(0,len(data)-i-1):
            if data[j][collumn] > data[j + 1][collumn]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if swapped == False:
            break
    return data

if __name__ == '__main__':
    sorted_data = sort(data, 2)
    print(sorted_data)