"""
Bir tamsayı sayısı dizisi ve bir tamsayı hedefi verildiğinde, iki sayının dönüş endeksleri, hedefe toplanacak şekilde.

Her girdinin tam olarak bir çözüme sahip olacağını varsayabilirsiniz ve aynı öğeyi iki kez kullanamazsınız.

Cevabı istediğiniz sırayla iade edebilirsiniz.
---------------------------------------------------------------------
Örnek 1:

Giriş: nums = [2,7,11,15], hedef = 9

Çıktı: [0,1]

Açıklama: Nums[0] + nums[1] == 9 nedeniyle [0, 1] döndürürüz.

---------------------------------------------------------------------
Örnek 2:

Giriş: sayılar = [3,2,4], hedef = 6

Çıktı: [1,2]

"""

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_control = {} 

        for i in range(len(nums)):

            control = target - nums[i]

            if control in nums_control.keys():

                return [nums_control[control],i]

            else:

                nums_control[nums[i]] = i
