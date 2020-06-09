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
