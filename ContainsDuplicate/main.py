"""
Bir tamsayı dizi sayıları verildiğinde, herhangi bir değer dizide en az iki kez görünüyorsa true döndürün ve her öğe farklıysa false döndürün.

------------------------------------------------------------------------------

Örnek 1:

Giriş: nums = [1,2,3,1]

Çıktı: doğru

Açıklama:

Element 1, 0 ve 3 endekslerinde meydana gelir.
"""

class Solution(object):
    def containsDuplicate(self, nums):
       
       return len(nums) != len(set(nums))

        