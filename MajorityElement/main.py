"""
N boyutunda bir dizi sayısı verildiğinde, çoğunluk öğesini döndürün.

Çoğunluk unsuru, ⌊n / 2⌋ zamanlarından daha fazla görünen öğedir. Çoğunluk elemanının dizide her zaman var olduğunu varsayabilirsiniz.
--------------------------------------------------------------------------------
Örnek 1:

Giriş: nums = [3,2,3]

Çıktı: 3
--------------------------------------------------------------------------------
Örnek 2:

Giriş: nums = [2,2,1,1,1,2,2]

Çıktı: 2
"""
class Solution(object):
    def majorityElement(self, nums):
        count = 0
        result = 0

        for i in nums:

            if count == 0:
                result = i
            
            count += 1 if i == result else -1
        return result
        