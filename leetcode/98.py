'''
a BST is defined as follows:
1.The left subtree of a node contains only nodes with keys less than the node's key.
2.The right subtree of a node contains only nodes with keys greater than the node's key.
3.Both the left and right subtrees must also be binary search trees.
'''
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def isValidBST(self, root):
        def dfs(root) :
            if not root :
                return (0 , 0 , True)
            if not root.left and not root.right :
                return (root.val , root.val , True)
            min_1 = min_2 = 1<<32
            max_1 = max_2 = -(1<<32)
            flag_1 = flag_2 = flag = True
            if root.left :
                min_1 , max_1 , flag_1 = dfs(root.left)
            if root.right :
                min_2 , max_2 , flag_2 = dfs(root.right)
            if min_2<=root.val or max_1>=root.val:
                flag = False
            min_ = min(root.val ,min(min_1 , min_2))
            max_ = max(root.val ,max(max_1 , max_2))
            flag = flag and flag_1 and flag_2
            return (min_ , max_ , flag)
        x,y,ret = dfs(root)
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
    ret = Solution().isValidBST(root)
    print(ret)