"""
Bir dize s verildiğinde, s iyi bir dize ise true döndürün, aksi takdirde false döndürün.

Bir dize s, s'de görünen tüm karakterler aynı sayıda oluşuma sahipse (yani aynı frekansa) iyidir.

-------------------------------------------------------------------------------------------------

Örnek 1:

Giriş: s = "abacbc"

Çıktı: doğru

Açıklama: S'de görünen karakterler 'a', 'b' ve 'c'dir. Tüm karakterler s'de 2 kez ortaya çıkar.

 -------------------------------------------------------------------------------------------------

Örnek 2:

Giriş: s = "aaabb"

Çıktı: yanlış

Açıklama: s'de görünen karakterler 'a' ve 'b'dir.

'A' 3 kez, 'b' ise 2 kez meydana gelir, bu da aynı sayıda değildir.

"""

def areOccurrencesEqual(s):

        dict = {}

        for i in s:

            if i in dict:

                dict[i] += 1

            else:

                dict[i] = 1
        
        return len(set(dict.values())) == 1
        
