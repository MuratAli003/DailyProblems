class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        left = right = head
        index = 0

        while right:
            right = right.next
            index += 1
        
        midIndex = index // 2 if index % 2 == 0 else index // 2 + 1

        while index > midIndex:
            left = left.next
            index -= 1 
        
        return left
        



             
        