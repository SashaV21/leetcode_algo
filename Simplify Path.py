class Solution(object):
    def simplifyPath(self, path):
        components = path.split('/')
        stack = []
        for elem in components:
            if elem == '' or elem == '.':
                continue

            if elem == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(elem)

        return '/' + '/'.join(stack)