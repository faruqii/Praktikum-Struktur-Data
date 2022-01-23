class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    file = open("SAMPLE DATA.txt", "r")
    stackData = file.readline()

    stackPunc = Stack()
    stackClean = Stack()

    punc = ".,!@#$%^&*)(}{-_=+][|':;<>/"

    length = len(stackData)-1
    while length >= 0:
        if stackData[length] in punc:
            stackPunc.push(stackData[length])
        else:
            stackClean.push(stackData[length])
        length -= 1

    print("Output Clean:")
    for i in range(stackClean.size()):
        print(stackClean.pop(), end="")

    print("\n\nOutput Punc:")
    for i in range(stackPunc.size()):
        print(stackPunc.pop(), end="")