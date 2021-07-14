class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def solution(root):
    #write your solution here
        
    def checkForRange(tree):
        if tree.val > 3 and tree.left:
            if checkForRange(tree.left): return True
        elif tree.val < -3 and tree.right:
            if checkForRange(tree.right): return True
        elif -3 <= tree.val <= 3: 
            return True

    return checkForRange(root)

tree = TreeNode(3)

print(solution(tree))
