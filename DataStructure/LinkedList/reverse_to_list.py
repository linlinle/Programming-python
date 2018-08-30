#-*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        pre_header = listNode
        result = []
        while pre_header != None:
            # result.append(pre_header.val)         # return result[::-1] or result.reverse()
            result.insert(0,pre_header.val)
            pre_header = pre_header.next

        return result

    def printListFromTailToHead_1(self, listNode):
        #   递归的方法
        if listNode is not None:
            return list(self.printListFromTailToHead_1(listNode.next))+ list([listNode.val])
        else:
            return []

if __name__ == "__main__":
    solution = Solution()
    Node_1 = ListNode(1)
    Node_2 = ListNode(2)
    Node_3 = ListNode(3)
    Node_1.next = Node_2
    Node_2.next = Node_3

    print(solution.printListFromTailToHead_1(Node_1))