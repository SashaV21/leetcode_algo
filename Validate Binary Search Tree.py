class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution(object):
#     def isValidBST(self, root):
#         def dfs(root, l, r):
#             if not root:
#                 return True
#             return l < root.val < r and dfs(root.left, l, root.val) and dfs(root.right, root.val, r)
#
#         return dfs(root, -(2 ** 31), (2 ** 31 - 1))

def isValidBST(self, root):
    queue = [(root, None, None)]

    while queue:
        node, lower, upper = queue.pop(0)

        if node is None:
            continue

        val = node.val
        if lower is not None and val <= lower:
            return False
        if upper is not None and val >= upper:
            return False

        queue.append((node.right, val, upper))

        queue.append((node.left, lower, val))

    return True