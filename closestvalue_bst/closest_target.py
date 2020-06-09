#function that takes in a BST and a target int value and returns 
#closest value to that target value contained in the BST

#recursive method

def closestBST(tree, target):
    return closestBSTHelper(tree, target, float("inf")) #initializing the helper method

def closestBSTHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return closestBSTHelper(tree.left, target, closest)
    elif target > tree.value:
        return closestBSTHelper(tree.right, target, closest)
    else:
        return closest

#iterative method
def closestBst(tree, target):
    return closestBstHelper(tree, target, float("inf"))

def closestBstHelper(tree, target, closest):
    while tree is not None:
        currenNode = tree
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currenNode.left
        elif target > currentNode.value:
            currenNode = currentNode.right
        else:
            break
    return closest 
