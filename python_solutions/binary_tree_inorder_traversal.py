from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    values = []
    stack = [root]
    while root and root.left:
        stack.append(root.left)
        root = root.left

    while stack:
        node = stack.pop()

        right_node = node.right
        if right_node:
            stack.append(right_node)
            while right_node.left:
                stack.append(right_node.left)
                right_node = right_node.left

        values.append(node.val)

    return values


if __name__ == '__main__':
    # head = TreeNode(2, TreeNode(1), TreeNode(3))
    head = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    ans = inorderTraversal(head)
    print(ans)
