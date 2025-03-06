"""
Bir tamsayı sayısı dizisi verildiğinde, iyi çiftlerin sayısını döndürün.

Bir çift (i, j) nums[i] == nums[j] ve i < j ise iyi olarak adlandırılır.
----------------------------------------------------------------------
Örnek 1:

Giriş: nums = [1,2,3,1,1,3]

Çıktı: 4

Açıklama: 4 iyi çift (0,3), (0,4), (3,4), (2,5) 0 endeksli vardır.
"""
public class Solution {
    public int NumIdenticalPairs(int[] nums) {
        int pairCount = 0;
        for(int i = 0; i < nums.Length; i++) {
            for(int j = i + 1; j < nums.Length; j++) {
                if(nums[i] == nums[j]) pairCount++;
            }
        }
        return pairCount;
    }
}