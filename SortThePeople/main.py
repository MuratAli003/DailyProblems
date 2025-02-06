"""
Size bir dizi dize adı ve farklı pozitif tam sayılardan oluşan bir dizi yüksekliği verilir. Her iki dizi de n uzunluğundadır.

Her i i dizini için isimler[i] ve yükseklikler[i], i. kişinin adını ve boyunu belirtir.

İnsanların boylarına göre azalan sırayla sıralanmış isimleri döndürün.

Örnek 1:

Giriş: isimler = ["Mary","John","Emma"], yükseklikler = [180,165,170]

Çıktı: ["Mary","Emma","John"]

Açıklama: Mary en uzun boylu, onu Emma ve John takip ediyor.

"""


def sortPeople(names, heights):
    
        result = []
        
        while len(names) > 0:

            indx = heights.index(max(heights))
            result.append(names[indx])

            heights.pop(indx)
            names.pop(indx)

        return result
