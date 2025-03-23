public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val=0, ListNode next=null) {
        this.val = val;
        this.next = next;
    }
}
 
public class Solution {
    public ListNode ModifiedList(int[] nums, ListNode head) {
        HashSet<int> numSet = new HashSet<int>(nums);
        ListNode left = head;
        ListNode right = head.next;

        while(right != null){
            if(numSet.Contains(right.val)){
                right = right.next;
            }
            else if(!numSet.Contains(right.val) && !numSet.Contains(left.val)){
                left.next = right;
                left = left.next;
                right = right.next;
            }
            else if(!numSet.Contains(right.val) && numSet.Contains(left.val)){
                left.val = right.val;
                left.next = right.next;
                right = right.next;
            }
        }
        left.next = right;
        return head;
    }
}