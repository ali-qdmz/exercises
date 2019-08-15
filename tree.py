class Tree:
    def __init__(self,cargo,left = None,right = None):
        self.cargo = cargo
        self.right = right
        self.left = left
    def __str__(self):
        return str(self.cargo)
def printTree(tree):
    if tree == None: return
    print(tree.cargo)
    printTree(tree.left)
    printTree(tree.right)

def printTreePostorder(tree):
    if tree == None: return
    printTreePostorder(tree.left)
    printTreePostorder(tree.right)
    print(tree.cargo)
def printTreeIndented(tree, level=0):
    if tree == None: return
    printTreeIndented(tree.right, level+1)
    print (' '*level + str(tree.cargo))
    printTreeIndented(tree.left, level+1)
