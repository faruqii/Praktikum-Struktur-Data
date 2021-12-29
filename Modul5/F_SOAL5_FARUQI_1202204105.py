import pandas as pd
import time

Algorithm = time.time()

class BubbleSort:
    def __init__(self, filename, collumn:int):
        self.filename = filename
        self.collumn = collumn

    def Sort(self):
        file = pd.read_csv(self.filename)
        file = file.values.tolist()
        
        if self.collumn == 0:
            print('\nSorted by Rank')
        elif self.collumn == 1:
            print('\nSorted By Title')
        elif self.collumn == 2:
            print('\nSorted by H-5 Index')
        elif self.collumn == 3:
            print('\nSorted by H-5 Median')

        for i in range(len(file)):
            swapped = False
            for j in range(0,len(file)-i-1):
                if file[j][self.collumn] > file[j + 1][self.collumn]:
                    file[j], file[j + 1] = file[j + 1], file[j]
                    swapped = True
            if swapped == False:
                break
               
        for sort in range(10):
            print(file[sort])

        print(f'Sort Algorithm Runtime: {time.time() - Algorithm} sec')

if __name__ == '__main__':
    Files = BubbleSort('Daspro.csv',3)
    Files.Sort()
