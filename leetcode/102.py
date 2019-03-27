class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def levelOrder(self, root):
        ret = []
        def dfs(root,level) :
            if not root :
                return 
            if len(ret)<level :
                ret.append([])
            ret[level-1].append(root.val)
            if root.left :
                dfs(root.left , level+1)
            if root.right :
                dfs(root.right , level+1)
        dfs(root,1)
        return ret
def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


if __name__ == '__main__':
    line = '[2,1,3]'
    root = stringToTreeNode(line)
    ret = Solution().levelOrder(root)
    print(ret)