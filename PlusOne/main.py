"""
Size bir tamsayı dizisi basamağı olarak temsil edilen büyük bir tam sayı verilir, burada her rakam[i] tam sayının i. basamağıdır. Rakamlar en önemliden en az önemliye doğru soldan sağa doğru sıralanır. Büyük tam sayı herhangi bir önde gelen 0 içermez.

Büyük tam sayıyı bir artırın ve ortaya çıkan basamak dizisini döndürün.

Örnek 1:

Giriş: basamak = [1,2,3]

Çıktı: [1,2,4]

Açıklama: Dizi, tamsayı 123'ü temsil eder.

Bir artış 123 + 1 = 124 verir.

Bu nedenle, sonuç [1,2,4] olmalıdır.
"""
class Solution(object):

    def plusOne(self, digits):
        
        for i in range(len(digits)-1,-1,-1):

            digits[i] += 1

            if digits[i] == 10:
                 digits[i] = 0

            else:

                return digits
        
        return [1] + digits
        