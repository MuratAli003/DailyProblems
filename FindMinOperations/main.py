"""
Size bir tamsayı dizisi sayıları verilir. Bir işlemde, herhangi bir num elementinden 1 ekleyebilir veya çıkarabilirsiniz.

Nums'in tüm öğelerini 3'e bölünebilir hale getirmek için minimum işlem sayısını döndürün.

---------------------------------------------------------------------------

Örnek 1:

Giriş: nums = [1,2,3,4]

Çıktı: 3

Açıklama:

Tüm dizi elemanları 3 işlem kullanılarak 3'e bölünebilir hale getirilebilir:

1'den 1'i çıkarın.

1'i 2'ye ekleyin.

4'ten 1'i çıkarın.
"""

def minimumOperations(nums):
        
    result = 0
    
    for i in nums:

        if i % 3 != 0:

            result += min(i%3, 3 - i%3)
                
    return result
