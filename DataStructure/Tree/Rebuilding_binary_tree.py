
"""输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。"""

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None


class Solution:
    def reConstructBinaryTree(self, pre, tin):
        """

        :param pre: 前向遍历
        :param tin: 中序遍历
        :return: 树结构
        """
        if not pre or not tin:
            return None
        root = TreeNode(pre.pop(0))
        index = tin.index(root.val)

        # 递归
        root.left = self.reConstructBinaryTree(pre,tin[:index])
        root.right = self.reConstructBinaryTree(pre,tin[index+1:])
        return root

if __name__=="__main__":
    solution = Solution()
    pre = [1,2,4,7,3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]
    tree = solution.reConstructBinaryTree(pre,tin)
    print(tree)


