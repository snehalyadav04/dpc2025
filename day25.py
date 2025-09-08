from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    def validate(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)
    return validate(root)

def build_tree(values):
    if not values or values[0] is None:
        return None
    iter_vals = iter(values)
    root = TreeNode(next(iter_vals))
    queue = deque([root])
    while queue:
        node = queue.popleft()
        try:
            left_val = next(iter_vals)
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)
            right_val = next(iter_vals)
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)
        except StopIteration:
            break
    return root

# Test Case 1
root = build_tree([2, 1, 3])
print("Input: root = [2, 1, 3]")
print("Output:", isValidBST(root))  
print()

# Test Case 2
root = build_tree([5, 1, 4, None, None, 3, 6])
print("Input: root = [5, 1, 4, null, null, 3, 6]")
print("Output:", isValidBST(root)) 
print()

# Test Case 3
root = build_tree([10, 5, 15, None, None, 6, 20])
print("Input: root = [10, 5, 15, null, null, 6, 20]")
print("Output:", isValidBST(root))  
print()
