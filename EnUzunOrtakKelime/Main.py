"""
Bir dizi dize arasında en uzun ortak kelime dizesini bulmak için bir işlev yazın.

Ortak bir dize yoksa, boş bir dize "" döndürün.

Örnek:

Giriş: strs = ["flower","flow","flight"]

Çıktı: "fl"

"""


from xmlrpc.client import boolean


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


