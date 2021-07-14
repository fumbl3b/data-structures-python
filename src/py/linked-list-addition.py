# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        s1, s2 = [], []
        
        currNode = l1
        while currNode.next:
          s1.append(currNode.val)
          currNode = currNode.next
        currNode = l2
        while currNode.next:
          s2.append(currNode.val)
          currNode = currNode.next
        
        return (s1,s2)


test = Solution()
test1 = ListNode()
test1.val = 5
test1.next = ListNode()
test1.next.val = 6
print(test1)

# print(test.addTwoNumbers(test1,test2))
