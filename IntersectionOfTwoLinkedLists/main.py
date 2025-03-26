"""
İki tek bağlantılı liste headA ve headB'nin başları göz önüne alındığında, iki listenin kesiştiği düğümü döndürün. Bağlantılı iki listenin hiç kesişimi yoksa, boş döndürün.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        
        pointer1 = headA
        pointer2 = headB

        while pointer1 != pointer2:

            pointer1 = pointer1.next if pointer1 != None else headB
            pointer2 = pointer2.next if pointer2 != None else headA
        
        return pointer1
        