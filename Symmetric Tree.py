class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def lcr(self, root, way, color):
        if root.left:
            self.lcr(root.left, way, 1)
        way.append((root.val, color))
        if root.right:
            self.lcr(root.right, way, -1)

    def rcl(self, root, way, color):
        if root.right:
            self.rcl(root.right, way, 1)
        way.append((root.val, color))
        if root.left:
            self.rcl(root.left, way, -1)


    def isSymmetric(self, root):
        if (not root.left or not root.right) and not (not root.left and not root.right):
            return False
        elif not root.left and not root.right:
            return True

        way_left = []
        way_right= []

        self.lcr(root.left, way_left, 0)
        self.rcl(root.right, way_right, 0)

        if way_right == way_left:
            return True
        else:
            return False
