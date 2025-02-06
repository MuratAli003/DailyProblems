"""
Size bir dize s verilir.

Göreviniz, bu işlemi tekrar tekrar yaparak tüm rakamları kaldırmaktır:

İlk rakamı ve solundaki en yakın rakam olmayan karakteri silin.

Tüm rakamları kaldırdıktan sonra ortaya çıkan dizeyi döndürün.

Örnek 1:

Input: s = "abc34"

Output: "a"

"""

def clearDigits(self, s):
        
        result = []

        for i in s:

            if i.isdigit() and result:

                result.pop()

            else:
                result.append(i)
        
        return "".join(result)
