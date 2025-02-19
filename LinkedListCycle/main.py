class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head:
            return False
        x = head
        y = head.next

        while x and y:
            x = x.next
            y = y.next
            if not y:
                return False
            y = y.next
            if x and y and x == y:
                return True
            
        return False