'''
https://algo.monster/liteproblems/124
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, res):
            if not node:
                return 0
            left_max = max(0, dfs(node.left, res))
            right_max = max(0, dfs(node.right, res))

            res[0] = max(res[0], node.val + left_max + right_max)
            return node.val + max(left_max, right_max)

        res = [float('-inf')]
        dfs(root, res)
        return res[0]
