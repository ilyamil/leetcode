from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
    if not left or not right:
        return left == right

    if left.val != right.val:
        return False

    return isMirror(left.right, right.left) and isMirror(left.left, right.right) 


def isSymmetric(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    return isMirror(root.left, root.right)


if __name__ == '__main__':
    node = TreeNode()