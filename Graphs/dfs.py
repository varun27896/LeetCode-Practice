class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add_child(self,name):
        self.children.append(Node(name))
        return self
    
    def dfs(self, array):
        array.append(self.name)
        for child in self.children:
            child.dfs(array)
        return array 
    