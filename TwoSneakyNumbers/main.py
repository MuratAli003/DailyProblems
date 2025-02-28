"""
Digitville kasabasında, 0'dan n - 1'e kadar tam sayıları içeren nums adı verilen sayıların bir listesi vardı. Her sayının listede tam olarak bir kez görünmesi gerekiyordu, ancak iki yaramaz sayı ek bir süre içinde gizlice girdi ve listeyi normalden daha uzun hale getirdi.

Kasaba dedektifi olarak göreviniz bu iki sinsi numarayı bulmaktır. İki sayıyı içeren iki boyutlu bir diziyi (herhangi bir sırayla) döndürün, böylece huzur Digitville'e geri dönebilir.
-----------------------------------------------------------------------------------------
Örnek 1:

Giriş: nums = [0,1,1,0]

Çıktı: [0,1]

Açıklama:

0 ve 1 sayılarının her biri dizide iki kez görünür.
"""
class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0,0]
        i = 0
        while nums:
            num = nums.pop(0)
            if num in nums:
                result[i] = num
                i+=1
        return result