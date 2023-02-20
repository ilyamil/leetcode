from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def validate(root: Optional[TreeNode], less_than=float('inf'), large_than=float('-inf')) -> bool:
    if not root:
        return True
    
    if root.val >= less_than or root.val <= large_than:
        return False
  
    left = validate(root.left, min(less_than, root.val), large_than)
    right = validate(root.right, less_than, max(root.val, large_than))
    return left and right


def isValidBST(root: Optional[TreeNode]) -> bool:
    return validate(root)
