# directory can only has 2 sub-dir
class Directory:
    def __init__(self, name: str):
        self.name = name
        self.childLeft = None
        self.childRight = None
    
    def __repr__(self):
        return f'{self.name}' 
    
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
        self.dirs = list()
    
    def create_root_dir(self, name):
        if self.root is None:
            self.root = Directory(name)
            self.dirs.append(self.root)
            return f'Succesful Created {name} Folder!'
    
    def create_child_directory(self, parent_directory_name: str, new_directory: Directory):
        # find given parent_directory
        par_directory = None 
        for dir in self.dirs:
            if str(dir) == parent_directory_name:
                par_directory = dir

        if par_directory is None:
            print(f"{parent_directory_name} directory not found!")    
            return

        par_directory.add_subdirectory(new_directory)
        self.dirs.append(new_directory)
    
    def print_fs_tree(self):
        if self.root is None:
            print('Directory Is Empty!')

        self.print_directories(self.root)

    def print_directories(self, directory: Directory):
        if directory is None:
            return
        directory.print_name()
        if directory.childLeft:
            self.print_directories(directory.childLeft)
        if directory.childRight:
            self.print_directories(directory.childRight)

    def find_directory(self, directory_name: str):
        for dir in self.dirs:
            if str(dir) == directory_name:
                return f'{dir} Found!'
        return f'{directory_name} directory not found!'

    def delete_directory(self, directory_name: str):
        dir_to_delete = None
        for dir in self.dirs:
            if str(dir) == directory_name:
                dir_to_delete = dir
                break

        if dir_to_delete is None: 
            print(f"{directory_name} directory not found!\nNothing to delete")    
            return

        # find parent directory
        parent_dir = None
        for dir in self.dirs:
            if dir.childLeft == dir_to_delete or dir.childRight == dir_to_delete:
                parent_dir = dir
                break

        if parent_dir is None:
            self.root = None
            self.dirs.remove(dir_to_delete)
            return 

        if parent_dir.childLeft == dir_to_delete:
            parent_dir.childLeft = None
        else:
            parent_dir.childRight = None
        self.dirs.remove(dir_to_delete)
        print(f"{directory_name} directory is deleted!")

if __name__ == '__main__':
    fs = FileSystem()
    while True:
        print('\n1.Login To Computer')
        print('2.Exit')
        menus = int(input('Enter your choice: '))
        if menus == 1:
            userName = input('Enter Your Username: ')
            while True:
                print(f'''
                {userName} welcome to your computer!
                1. Create Root directory
                2. Add child to directory
                3. Print Directory
                4. Delete Directory
                5. Find Directory
                6.Logout
                ''')
                choice = input('Enter your choice: ')
                if choice == '1':
                    name = input('Enter directory name: ')
                    root_dir = Directory(name)
                    print(fs.create_root_dir(root_dir))
                elif choice == '2':
                    userInput = input('Create Sub directory (Target directory, Sub directory Name): ')
                    splitInput = userInput.split(',')
                    new_directory = Directory(splitInput[1])
                    fs.create_child_directory(splitInput[0], new_directory)
                elif choice == '3':
                    fs.print_fs_tree()
                elif choice == '4':
                    name = input('Enter directory name: ')
                    fs.delete_directory(name)
                elif choice == '5':
                    name = input('Enter directory name: ')
                    print(fs.find_directory(name))
                elif choice == '6':
                    UserAuth = input('Enter username: ')
                    if UserAuth == userName:
                        print('Logout Successful!')
                        print(f'See you again {userName}!')
                        break
                    else:
                        print('Wrong username!')
                else:
                    print('Invalid choice')
                    break
        elif menus == 2:
            print('Thank you for using this program')
            break