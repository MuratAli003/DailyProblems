"""
Her düğümün bir tamsayı değeri içerdiği bağlantılı bir liste başlığının başı verildiğinde.

Her bitişik düğüm çifti arasına, en büyük ortak bölenine eşit bir değere sahip yeni bir düğüm ekleyin.

Ekledikten sonra bağlantılı listeyi döndürün.

İki sayının en büyük ortak böleni, her iki sayıyı da eşit olarak bölen en büyük pozitif tam sayıdır.
"""
public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val=0, ListNode next=null) {
        this.val = val;
        this.next = next;
    }
}
public class Solution {
    public int EBOB(int num1, int num2){

        for(int i = Math.Min(num1,num2); i > 1; i--){
            if(num1%i == 0 && num2%i == 0){
                return i;
            }
        }
        return 1;
    }
    public ListNode InsertGreatestCommonDivisors(ListNode head) {
        
        ListNode left = head;
        ListNode right = head.next;

        while(right != null){
            ListNode newNode = new ListNode();
            left.next = newNode;
            newNode.next = right;
            newNode.val = EBOB(left.val,right.val);
            left = right;
            right = right.next;
        }
        return head;
    }
}