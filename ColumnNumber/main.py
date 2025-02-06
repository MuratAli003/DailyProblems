"""

Sütun başlığını bir Excel sayfasında göründüğü gibi temsil eden bir dize columnTitle verildiğinde, karşılık gelen sütun numarasını döndürün.

Örneğin:

A -> 1

B -> 2

C -> 3

...

Z -> 26

AA -> 27

AB -> 28

...

----------------------------

Örnek 1:

Giriş: columnTitle = "A"

Çıktı: 1

-----------------------------

Örnek 2:

Giriş: columnTitle = "AB"

Çıktı: 28

-----------------------------

Örnek 3:

Giriş: columnTitle = "ZY"

Çıktı: 701
"""

def titleToNumber(columnTitle):
       
        res = 0

        for i in range(len(columnTitle)):

            res += pow(26,(len(columnTitle) - i - 1)) * (ord(columnTitle[i]) - ord('A') + 1)
        
        return res
