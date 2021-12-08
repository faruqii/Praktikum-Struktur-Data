def removePunc(file):
    # Open file
    f = open(file, 'r')
    # And then read by lines
    lines = f.readlines()
    
    afterClean = []

    for line in lines:
        for word in line.split():
            newWord = ""
            for i, char in enumerate(word):
                if not char.isascii():
                    continue
                if char.isalnum():
                    newWord += char
            if newWord != "":
                newWord += " "
                afterClean.append(newWord)   
    
    afterClean.reverse()
    final = ""
    for _ in range(len(afterClean)):
        final += afterClean.pop()

    with open(file, 'w') as f2:
        f2.write(final)
    
    print("Cleansing Data Succesfull!\n",final)
        
if __name__ == "__main__":
    file = input("Enter file name: ")
    removePunc(file)

    