
"""
Geçerli bir parantez dizesi s verildiğinde, s'nin yuvalama derinliğini döndürün. Yuvalama derinliği, iç içe geçmiş parantezlerin maksimum sayısıdır.

Örnek 1:

Giriş: s = "(1+(2*3)+((8)/4))+1"

Çıktı: 3

Açıklama:

Rakam 8, dizedeki 3 iç içe parantezin içindedir.
"""

def maxDepth(s):
    
        count = 0
        result = 0

        for i in s:

            if i == "(":

                count += 1
            
            elif i == ")":

                result = max(count,result)
                count -= 1
        
        return result
