"""
Size 0'larla ayrılmış bir dizi tam sayı içeren bağlantılı bir listenin başı verilir. Bağlantılı listenin başında ve sonunda Node.val == 0 olacaktır.

Ardışık her iki 0 için, aralarında yatan tüm düğümleri, değeri birleştirilmiş tüm düğümlerin toplamı olan tek bir düğümde birleştirin. Değiştirilen liste herhangi bir 0 içermemelidir.

Değiştirilen bağlantılı listenin başını döndürün.
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
    public ListNode MergeNodes(ListNode head) {
        
        ListNode resultList = new ListNode();
        ListNode result = resultList;
        int zeroControl = 0;
        int total = 0;
        while(head != null){
            if(head.val == 0){
                zeroControl += 1;
            }
            if(zeroControl == 2){
                zeroControl -= 1;
                resultList.val = total;
                if(head.next != null){
                    resultList.next = new ListNode();
                    resultList = resultList.next;
                }
                total = 0;
            }
            total += head.val;
            head = head.next;
        }
    
        return result;
    }
}