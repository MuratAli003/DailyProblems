class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        num = 0
        head = resultList = ListNode()
        while l1 and l2:
            node = ListNode()
            total = l1.val + l2.val + num

            if total >= 10:
                node.val = total % 10
                num = 1

            else:
                node.val = total
                num = 0

            resultList.next = node
            resultList = resultList.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            node = ListNode()
            total = l1.val + num

            if total >= 10:
                node.val = total % 10
                num = 1

            else:
                node.val = total
                num = 0
            
            resultList.next = node
            resultList = resultList.next
            l1 = l1.next
        
        while l2:
            node = ListNode()
            total = l2.val + num

            if total >= 10:
                node.val = total % 10
                num = 1

            else:
                node.val = total
                num = 0
            
            resultList.next = node
            resultList = resultList.next
            l2 = l2.next
        
        if num == 1:
            node = ListNode()
            node.val = 1
            resultList.next = node
            resultList = resultList.next

        return head.next


            
            


