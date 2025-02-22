class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getDecimalValue(self , head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        left = right = head
        index = -1
        result = 0

        while right:
            right = right.next
            index += 1
        
        while left:
            result += pow(2,index) * left.val
            index -= 1
            left = left.next

        return result

