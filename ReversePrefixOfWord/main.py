"""
0 endeksli bir dize kelimesi ve bir ch karakteri verildiğinde, 0 dizininde başlayan ve ch'nin ilk oluşumunun (dahil) endeksinde biten kelimenin bölümünü tersine çevirin. Eğer ch karakteri word'de mevcut değilse, hiçbir şey yapmayın.

Örneğin, word = "abcdefd" ve ch = "d" ise, 0'da başlayan ve 3'te (dahil) biten bölümü tersine çevirmelisiniz. Ortaya çıkan dize "dcbaefd" olacaktır.

Ortaya çıkan dizeyi döndürün.


Örnek 1:

Giriş: word = "abcdefd", ch = "d"

Çıktı: "dcbaefd"

Açıklama: "d"nin ilk oluşumu indeks 3'tedir.

Kelimenin kısmını 0'dan 3'e (dahil) ters çevirin, ortaya çıkan dize "dcbaefd"dir.

"""

def reversePrefix(word, ch):
        
        result = []
        control = True
        for i in word:

            if i == ch and control:

                result.append(i)
                result = result[::-1]
                control = False
            
            else:
                result.append(i)

        return "".join(result)