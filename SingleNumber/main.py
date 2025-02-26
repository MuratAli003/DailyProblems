"""
Boş olmayan bir tamsayı sayısı dizisi verildiğinde, biri hariç her öğe iki kez görünür. O tek olanı bul.

Doğrusal çalışma zamanı karmaşıklığına sahip bir çözüm uygulamalı ve yalnızca sabit ekstra alan kullanmalısınız.
-------------------------------------------------------------------------------------------------
Örnek 1:

Giriş: nums = [2,2,1]

Çıktı: 1
-------------------------------------------------------------------------------------------------
Örnek 2:

Giriş: nums = [4,1,2,1,2]

Çıktı: 4
-------------------------------------------------------------------------------------------------
Örnek 3:

Giriş: sayılar = [1]

Çıktı: 1
"""
class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        print(nums)

        for i in range(0,len(nums)-1,2):


            if nums[i] != nums[i+1]:
                return nums[i]

        return nums[-1]
        