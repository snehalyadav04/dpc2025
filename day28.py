from typing import Optional, List
from collections import deque

null = None

class TreeNode:
    def __init__(self, val: Optional[int]=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    index = 1
    while queue and index < len(values):
        node = queue.popleft()
        if node:
            if index < len(values) and values[index] is not null:
                node.left = TreeNode(values[index])
                queue.append(node.left)
            index += 1
            if index < len(values) and values[index] is not null:
                node.right = TreeNode(values[index])
                queue.append(node.right)
            index += 1
    return root

def is_symmetric(root: Optional[TreeNode]) -> bool:
    def is_mirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (
            t1.val == t2.val and
            is_mirror(t1.left, t2.right) and
            is_mirror(t1.right, t2.left)
        )
    return is_mirror(root, root)

test_cases = [
    [1, 2, 2, 3, 4, 4, 3],
    [1, 2, 2, null, 3, null, 3],
    [1],
    [],
    [1, 2, 2, 3, null, null, 3]
]

for test in test_cases:
    tree = build_tree(test)
    result = is_symmetric(tree)
    formatted_input = str(test).replace("None", "null")
    print(f"Input: {formatted_input}")
    print(f"Output: {result}\n")
