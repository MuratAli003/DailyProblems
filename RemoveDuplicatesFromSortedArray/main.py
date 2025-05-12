"""
Azalmayan sırayla sıralanmış bir tamsayı dizisi numaraları verildiğinde, kopyaları yerinde kaldırın, böylece her benzersiz öğe yalnızca bir kez görünür. Elemanların göreceli sırası aynı tutulmalıdır. Ardından, nums olan benzersiz öğelerin sayısını döndürün.

Sayıların benzersiz elemanlarının sayısını k olarak düşünün, kabul edilmek için aşağıdakileri yapmanız gerekir:

Dizi nums'larını, nums'un ilk k elemanı, başlangıçta nums'ta mevcut oldukları sırayla benzersiz öğeleri içerecek şekilde değiştirin. Nums'un kalan elementleri, nums'ın boyutu kadar önemli değildir.

Dönüş k.

-----------------------------------------------------------------------
Örnek 1:

Giriş: sayılar = [1,1,2]

Çıktı: 2, nums = [1,2,_]

Açıklama: Fonksiyonunuz k = 2 döndürmeli, numların ilk iki elemanı sırasıyla 1 ve 2 olmalıdır.

İade edilen k'nin ötesinde ne bıraktığınız önemli değildir (dolayısıyla alt çizgidir).
-----------------------------------------------------------------------
"""

class Solution(object):
    def removeDuplicates(self, nums):
        k = 1  
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
                



        