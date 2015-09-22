# ****Main Function****
# ****Written by Andrew Nelson, November 2014****
# ****For CS260 Programming Assignment 3****
# ****This class serves as the main function for the assignment****

from bst import *

def main():
    tree = eval(input("Enter level-order as a Python list: "))
    bst = BST(tree)

    for i in tree:
        bst.add(i)
    
    print("In-Order:    ",bst.inOrder())
    print("Pre-Order:   ",bst.preOrder())
    print("Post-Order:  ",bst.postOrder())
    print("Level-Order: ",bst.levelOrder())

main()    
