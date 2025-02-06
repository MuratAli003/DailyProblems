"""
Azalmayan sırayla sıralanmış bir tamsayı sayısı dizisi verildiğinde, belirli bir hedef değerin başlangıç ve bitiş konumunu bulun.

Hedef dizide bulunmazsa, [-1, -1] döndürün.

O(log n) çalışma zamanı karmaşıklığına sahip bir algoritma yazmalısınız.

Örnek 1:

Giriş: nums = [5,7,7,8,8,10], hedef = 8

Çıktı: [3,4]

"""


def searchRange(self, nums, target):
        
        left = 0
        right = len(nums)-1

        start = 0
        end = 0

        while left <= right:

            mid = int((left + right) / 2)

            if nums[mid] == target:

                i = mid
                j = mid

                while i>=0 or j < len(nums):
                    if i >= 0 and nums[i] == target:
                        start = i
                        i -= 1
                    if j < len(nums) and nums[j] == target:
                        end = j
                        j += 1
                    if (i < 0 or nums[i] != target) and (j >= len(nums) or nums[j] != target):
                        break

                return [start,end]
            
            elif nums[mid] < target:

                left = mid + 1
            
            else:

                right = mid-1

        return [-1,-1]
