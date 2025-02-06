class ListNode(object):
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
       
class Solution(object):
    def isPalindrome(self, head):
        
        newList = []

        x = head
        while x:

            newList.append(x.val)

            x= x.next

        return newList == newList[::-1]