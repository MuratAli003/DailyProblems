"""
Sadece dört işlem ve bir değişken X içeren bir programlama dili vardır:

++X ve X++, X değişkeninin değerini 1 artırır.

--X ve X--, X değişkeninin değerini 1'e azaltır.

Başlangıçta, X'in değeri 0'dır.

Bir işlem listesi içeren bir dizi dize işlemi verildiğinde, tüm işlemleri gerçekleştirdikten sonra X'in son değerini döndürün.
-----------------------------------------------------------------------------------
Örnek 1:

Giriş: işlemler = ["--X","X++","X++"]

Çıktı: 1
-----------------------------------------------------------------------------------
Açıklama: İşlemler aşağıdaki gibi gerçekleştirilir:

* Başlangıçta, X = 0.

* --X: X 1, X = 0 - 1 = -1 azalır.

* X++: X 1, X = -1 + 1 = 0 artar.

* X++: X 1 artar, X = 0 + 1 = 1 artar.
"""
public class Solution {
    public int FinalValueAfterOperations(string[] operations) {
        
        int result = 0;

        for(int i = 0;i <operations.Length;i++){
            if(operations[i][1] == '+'){
                result += 1;
            }
            else{
                result -= 1;
            }
        }
        return result;
    }
}