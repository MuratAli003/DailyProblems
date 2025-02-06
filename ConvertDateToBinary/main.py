"""
Size yyyy-aa-gg biçiminde bir Gregoryen takvim tarihini temsil eden bir dize tarihi verilir.

Tarih, yıl, ay ve gün herhangi bir önde sıfır olmadan ikili temsillerine dönüştürülerek ve bunları yıl-ay-gün biçiminde yazarak elde edilen ikili gösteriminde yazılabilir.

Tarihin ikili gösterimini döndürün.

Örnek 1:

Giriş: tarih = "2080-02-29"

Çıktı: "100000100000-10-11101"

Açıklama:

1000000000000, 10 ve 11101, sırasıyla 2080, 02 ve 29'un ikili temsilleridir.

"""


def convertDateToBinary(date):
        """
        :type date: str
        :rtype: str
        """
        date = date.split("-")
        result = []
        for i in date:

            binaryStack = []

            i = int(i)
            while i > 0:

                binaryStack.insert(0,i%2)
                i /= 2
            
            num = "".join(map(str,binaryStack))
            result.append(num)
        
        return "-".join(result)
