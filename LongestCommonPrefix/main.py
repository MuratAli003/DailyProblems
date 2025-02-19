"""
Bir dizi dize arasında en uzun ortak önek dizesini bulmak için bir işlev yazın.

Ortak bir önek yoksa, boş bir dize "" döndürün.

-----------------------------------------------------------
Örnek 1:

Giriş: strs = ["çiçek","akış","uçuş"]

Çıktı: "fl"

-----------------------------------------------------------
Örnek 2:

Giriş: strs = ["köpek","yarış arabası","araba"]

Çıktı: ""

Açıklama: Giriş dizeleri arasında ortak bir önek yoktur.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:

            return strs[0]

        else:

            cevap = ""
            strs.sort()

            uzunluk = min(len(strs[0]), len(strs[len(strs) - 1]))
            j = 0

            kontrol = True

            while (j < uzunluk):

                gecici = ""
                for k in range(0, len(strs) - 1):

                    gecici = strs[k][j]
                    if strs[k][j] != strs[k + 1][j]:
                        kontrol = False
                        break

                if kontrol:

                    cevap += gecici

                else:

                    break

                j += 1

            return cevap
