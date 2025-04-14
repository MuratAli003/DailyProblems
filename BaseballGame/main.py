"""
Garip kuralları olan bir beyzbol maçı için puanları tutuyorsunuz. Oyunun başında boş bir kayıtla başlarsınız.

Size dize işlemlerinin bir listesi verilir, burada işlemler[i] kayda uygulamanız gereken it. işlemdir ve aşağıdakilerden biridir:

Bir tam sayı x.

Yeni bir x puanı kaydedin.

'+': Önceki iki puanın toplamı olan yeni bir puan kaydedin.

'D': Önceki puanın iki katı olan yeni bir puan kaydedin.

'C': Önceki puanı geçersiz kılın, kayıttan kaldırın.

Tüm işlemleri uyguladıktan sonra kayıttaki tüm puanların toplamını döndürün.

Test durumları, cevabın ve tüm ara hesaplamaların 32 bitlik bir tam sayıya sığacak ve tüm işlemlerin geçerli olduğu şekilde oluşturulur.
----------------------------------------------------------------------------------------
Örnek 1:

Giriş: ops = ["5","2","C","D","+"]

Çıktı: 30

Açıklama:

* "5" - Kayda 5 ekleyin, kayıt şimdi [5].

* "2" - Kayda 2 ekleyin, kayıt şimdi [5, 2].

* "C" - Önceki puanı geçersiz kılın ve kaldırın, kayıt şimdi [5].

* "D" - Kayda 2 * 5 = 10 ekleyin, kayıt şimdi [5, 10].

* "+" - Kayda 5 + 10 = 15 ekleyin, kayıt şimdi [5, 10, 15].

Toplam toplam 5 + 10 + 15 = 30'dur.
"""
class Solution(object):
    def calPoints(self, operations):
        
        result = 0
        scores =[]

        for i in operations:

            if i == "C":
                
                result -= scores.pop()


            
            elif i == "D":

                score = 2 * scores[-1]
                scores.append(score)
                result += score
            
            elif i == "+":

                score = scores[-1] + scores[-2]
                scores.append(score)
                result += score
                
            else:

                scores.append(int(i))
                result += int(i)
        
        return result