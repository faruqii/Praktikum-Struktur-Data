class Directory:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class DirectorySystem:
    def __init__(self):
        self.root = None
        self.current = None

    def create_folder(self, name):
        if self.root is None:
            self.root = Directory(name)
            self.current = self.root
        else:
            self.current = self.root
            self.create_folder(name)

    def create_folder_child(self, target_folder, folder_name):
        if target_folder is None:
            print('Target Folder Is Empty')

        if target_folder.left is None:
            target_folder.left = Directory(folder_name)
        elif target_folder.right is None:
            target_folder.right = Directory(folder_name)
        else:
            print("Folder is full")
        
    def print_tree_traversal(self):
        if self.root is None:
            print("Folder is Empty")
        else:
            self.print_parent(self.root)
            self.print_tree_traversal_recursive(self.root) 


    def print_parent(self, Directory):
        if Directory is None:
            return
        print(f'\t{Directory.name}')

    def print_tree_traversal_recursive(self, Directory, i=0):
        if Directory is None:
            return
        self.print_tree_traversal_recursive(Directory.left, i+1)
        self.print_tree_traversal_recursive(Directory.right, i+1)
        if i != 0:
            print(Directory.name, end=' ')

    def search_folder(self, folder_name):
        if self.root is None:
            print("Folder is Empty")
        else:
            self.search_folder(folder_name)
            print(f"Folder {folder_name} is found!")
    
if __name__ == '__main__':
    app = DirectorySystem()
    while True:
        print('''
        1. Create folder Root
        2. Create folder child  of Root
        3. Print tree
        4. Search Tree
        ''')
        choice = input('Enter your choice: ')
        if choice == '1':
            name = input('Enter folder name: ')
            app.create_folder(name)
        elif choice == '2':
            userInput = input('Create Sub Folder (Target Folder, Sub Folder Name): ')
            splitInput = userInput.split(',')
            app.create_folder_child(app.root,splitInput[1])
        elif choice == '3':
            app.print_tree_traversal()
        elif choice == '4':
            folder_name = input('Enter folder name: ')
            app.search_folder(folder_name)
        else:
            print('Invalid choice')
            break