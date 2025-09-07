from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

def find_node(root: TreeNode, val: int) -> Optional[TreeNode]:
    if root is None:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    return left if left else find_node(root.right, val)

def lowestCommonAncestor(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right

test_cases = [
    ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4),
    ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1),
    ([1, 2], 1, 2)
]

for values, p_val, q_val in test_cases:
    root = build_tree(values)
    p = find_node(root, p_val)
    q = find_node(root, q_val)
    lca = lowestCommonAncestor(root, p, q)
    print(f"Input: root = {values}, p = {p_val}, q = {q_val}")
    print(f"Output: {lca.val}\n")
