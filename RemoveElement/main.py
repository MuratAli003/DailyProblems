"""
Bir tamsayı dizisi nums ve bir tamsayı val verildiğinde, nums içindeki tüm val oluşumlarını yerinde kaldırın. Öğelerin sırası değiştirilebilir. Ardından, val'e eşit olmayan sayılardaki öğelerin sayısını döndürün.

Nums içindeki val be k'ye eşit olmayan elemanların sayısını düşünün, kabul edilmek için aşağıdakileri yapmanız gerekir:

Dizi numlarını, nums'in ilk k elemanının val'e eşit olmayan öğeleri içermesi için değiştirin. Nums'un kalan elementleri, nums'ın boyutu kadar önemli değildir.

Örnek 2:

Giriş: nums = [0,1,2,2,3,0,4,2], val = 2

Çıktı: 5, nums = [0,1,4,0,3,_,_,_]

Açıklama: Fonksiyonunuz, numların ilk beş elemanı 0, 0, 1, 3 ve 4 içeren k = 5 döndürmelidir.

    Beş öğenin herhangi bir sırayla iade edilebileceğini unutmayın.

    İade edilen k'nin ötesinde ne bıraktığınız önemli değildir (dolayısıyla alt çizgidir).
}
"""
class Solution(object):
    def removeElement(self, nums, val):
        
        k = 0

        i = 0

        while i < len(nums) :

            if nums[i] == val:
                nums.pop(i)
            else:
                i+=1
                k+=1
        return k    