"""
N kutun var. Size n uzunluğunda bir ikili dize kutusu verilir, burada boxs[i] ith kutusu boşsa '0' ve bir top içeriyorsa '1'.

Bir işlemde, bir topu bir kutudan bitişik bir kutuya taşıyabilirsiniz. Kutu i, abs(i - j) == 1 ise kutu j'ye bitişiktir. Bunu yaptıktan sonra, bazı kutularda birden fazla top olabileceğini unutmayın.

N boyutunda bir dizi cevabı döndürün, burada cevap[i], tüm topları ith kutusuna taşımak için gereken minimum işlem sayısıdır.

Her cevap[i], kutuların başlangıç durumu dikkate alınarak hesaplanır.
---------------------------------------------------------------------------------------------
Örnek 1:

Giriş: kutular = "110"

Çıktı: [1,1,3]

Açıklama: Her kutu için cevap aşağıdaki gibidir:

1) İlk kutu: tek bir işlemde bir topu ikinci kutudan ilk kutuya taşımanız gerekecektir.

2) İkinci kutu: tek bir işlemde bir topu ilk kutudan ikinci kutuya taşımanız gerekecektir.

3) Üçüncü kutu: iki işlemde bir topu ilk kutudan üçüncü kutuya taşımanız ve bir işlemde bir topu ikinci kutudan üçüncü kutuya taşımanız gerekecektir.
"""
class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        result = len(boxes)*[0]

        numDicts = {}

        for i,char in enumerate(boxes):
            if char == "1":
                numDicts[i] = 1

        for j in range(len(result)):
            for k in numDicts.keys():
                result[j] += abs(j-k)
                
        return result
            

      