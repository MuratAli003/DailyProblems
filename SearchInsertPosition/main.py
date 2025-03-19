"""
Farklı tam sayılardan oluşan sıralanmış bir dizi ve bir hedef değer verildiğinde, hedef bulunursa dizini döndürün. Değilse, dizini sırayla eklenmiş olsaydı olacağı yere döndürün.

O(log n) çalışma zamanı karmaşıklığına sahip bir algoritma yazmalısınız.
---------------------------------------------------------------------
Örnek 1:

Giriş: nums = [1,3,5,6], hedef = 5

Çıktı: 2
---------------------------------------------------------------------
Örnek 2:

Giriş: nums = [1,3,5,6], hedef = 2

Çıktı: 1
"""
class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)-1

        while left <= right:

            median = int((left+right) / 2)

            if nums[median] == target:
                return median
            
            elif nums[median] < target:

                left = median+1
            
            else:
                right = median-1
        
        return left
            