"""
Bağlantılı bir listenin başı göz önüne alındığında, n. düğümü listenin sonundan kaldırın ve başını döndürün.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        leftControl = head
        rightControl = head

        while n > 0:

            rightControl = rightControl.next
            n-=1
        
        while rightControl and rightControl.next:
            rightControl = rightControl.next
            leftControl = leftControl.next

        if leftControl and not rightControl:
            return leftControl.next

        leftControl.next = leftControl.next.next
        return head