class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data_target, new_data):
        if self.data == data_target:
            if self.left is None:
                self.left = Node(new_data)
            elif self.right is None:
                self.right = Node(new_data)
        elif self.data != data_target:
            if self.left.data == data_target:
                self.left.insert(data_target, new_data)
            elif self.right.data == data_target:
                self.right.insert(data_target, new_data)
            # else:
            #     self.left.insert(data_target, new_data)

def preorder(root):
    if root == None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)  

root = Node("folder_utama")
root.insert("folder_utama", "strukdat")
root.insert("folder_utama", "basdat")
root.insert("strukdat", "nilai_strukdat")
root.insert("strukdat", "video_strukdat")
root.insert("basdat", "nilai_basdat")
root.insert("basdat", "video_basdat")
root.insert("video_basdat", "saya")

preorder(root)