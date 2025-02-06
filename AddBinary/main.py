"""
İki ikili dize a ve b verildiğinde, toplamlarını ikili bir dize olarak döndürür.

Örnek 1:

Giriş: a = "11", b = "1"

Çıktı: "100"

Örnek 2:

Giriş: a = "1010", b = "1011"

Çıktı: "10101

"""

def addBinary(a, b):

        numA = 0
        numB = 0

        for i in range(len(a)-1,-1,-1):

            numA += pow(2,(len(a)-1 - i)) * int(a[i])
        
        for i in range(len(b)-1,-1,-1):

            numB += pow(2,(len(b)-1 - i)) * int(b[i])
        
        res = numA + numB

        res = bin(res)
        
        return res[2:len(res)]
