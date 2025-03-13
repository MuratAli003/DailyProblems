"""
Pozitif bir tam sayı n verildiğinde, hem 2 hem de n'nin katı olan en küçük pozitif tam sayıyı döndürün.
----------------------------------------------------------------------------
Örnek 1:

Giriş: n = 5

Çıktı: 10

Açıklama: Hem 5 hem de 2'nin en küçük katı 10'dur.
----------------------------------------------------------------------------
Örnek 2:

Giriş: n = 6

Çıktı: 6

Açıklama: Hem 6 hem de 2'nin en küçük katı 6'dır. Bir sayının kendisinin bir katı olduğuna dikkat edin.

"""
public class Solution {
    public int SmallestEvenMultiple(int n) {
        
        if(n%2 == 0){
            return n;
        }
        else{
            return n*2;
        }
    }
}