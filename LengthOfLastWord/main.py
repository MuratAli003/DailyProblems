"""
Kelimelerden ve boşluklardan oluşan bir dize s verildiğinde, dizedeki son kelimenin uzunluğunu döndürün.

Bir kelime, yalnızca boşluk dışı karakterlerden oluşan maksimum bir alt dizedir.
--------------------------------------------------------------------------------
Örnek 1:

Giriş: s = "Merhaba Dünya"

Çıktı: 5

Açıklama: Son kelime 5 uzunluğundaki "Dünya"dır.
--------------------------------------------------------------------------------
Örnek 2:

Giriş: s = " beni aya uçur "

Çıktı: 4

Açıklama: Son kelime 4 uzunluğunda "ay"dır.
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        
        result = 0
        s = s.strip()
        for i in s:

            if i ==" ":
                result = 0
            else:
                result += 1

        return result
        