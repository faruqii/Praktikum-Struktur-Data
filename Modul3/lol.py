# directory can only has 2 sub-dir
class Directory:
    def __init__(self, name: str):
        self.name = name
        self.childLeft = None
        self.childRight = None
    
    def add_subdirectory(self, directory):
        if self.childLeft is None:
            self.childLeft = directory
        elif self.childRight is None:
            self.childRight = directory
        else:
           print("directory is full")
    
    def print_name(self):
        print(self.name)

class FileSystem:
    def __init__(self):
        self.root = None
    
    def create_root_dir(self, name):
        if self.root is None:
            self.root = Directory(name)
            return
    
    def create_child_directory(self, parent_directory_name: str, new_directory: Directory):
        # find given parent_directory
        found, par_directory = self.find_directory(parent_directory_name,self.root)
        if not found:
            print("parent directory not found")

        if par_directory is None:
            print('Target directory Is Empty')
            return
        
        par_directory.add_subdirectory(new_directory)
    
    def print_fs_tree(self):
        if self.root is None:
            return 'Folder is empty!'
        self.root.print_name()

        self.print_directories(self.root)

    def print_directories(self, directory: Directory):
        if directory is None:
            return 
        # start with left child
        if directory.childLeft:
            self.print_directories(directory.childLeft)
        directory.print_name()
        if directory.childRight:
            self.print_directories(directory.childRight)
    
    def find_directory(self, directory_name: str, directory: Directory):
        if directory_name is None:
            return False, None
        
        if self.root is None:
            return False, None
        
        if directory.childLeft:
            self.find_directory(directory.name, directory.childLeft)
        
        if directory.name is directory_name:
            return True, directory

        if directory.childRight:
            self.find_directory(directory.name, directory.childRight)

if __name__ == '__main__':
    fs = FileSystem()
    while True:
        print('''
        1. Create Root directory
        2. Add child to directory
        3. Print tree
        ''')
        choice = input('Enter your choice: ')
        if choice == '1':
            name = input('Enter directory name: ')
            root_dir = Directory(name)
            fs.create_root_dir(root_dir)
        elif choice == '2':
            userInput = input('Create Sub directory (Target directory, Sub directory Name): ')
            splitInput = userInput.split(',')
            new_directory = Directory(splitInput[1])
            fs.create_child_directory(splitInput[0], new_directory)
        elif choice == '3':
            print(fs.print_fs_tree())
        else:
            print('Invalid choice')
            break