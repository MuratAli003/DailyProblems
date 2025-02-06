"""
Artan sırayla sıralanmış bir tamsayı sayısı dizisi ve bir tamsayı hedefi verildiğinde, hedefi sayılarda aramak için bir işlev yazın. Hedef varsa, indeksini döndürün. Aksi takdirde, -1'i döndürün.

O(log n) çalışma zamanı karmaşıklığına sahip bir algoritma yazmalısınız.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

"""

def search(nums, target):
        
        left = 0
        right = len(nums)-1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:

                return mid
            
            elif nums[mid] < target:

                left = mid + 1
            
            else:

                right = mid - 1
        
        return -1
