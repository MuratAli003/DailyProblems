"""
Size pozitif tam sayılar n ve m verilir.

İki tam sayıyı aşağıdaki gibi tanımlayın:

Num1: [1, n] (her ikisi de dahil) aralığındaki m'ye bölünemeyen tüm tam sayıların toplamı.

Num2: [1, n] (her ikisi de dahil) aralığındaki ve m'ye bölünebilen tüm tam sayıların toplamı.

Tamsayı num1 - num2'yi döndürün.
---------------------------------------------------------------------------------------------
Örnek 1:

Giriş: n = 10, m = 3

Çıktı: 19

Açıklama: Verilen örnekte:

* [1, 10] aralığında 3'e bölünemeyen tam sayılar [1,2,4,5,7,8,10], num1 bu tam sayıların toplamıdır = 37.

* [1, 10] aralığında 3'e bölünebilen tam sayılar [3,6,9], num2 bu tam sayıların toplamıdır = 18.

Cevap olarak 37 - 18 = 19 döndürüyoruz.
"""
public class Solution {
    public int DifferenceOfSums(int n, int m) {
        
        int num1 = 0;
        int num2 = 0;

        for(int i= 1; i<=n; i++){
            if(i % m == 0){
                num2 += i; 
            }
            else{
                num1 += i;
            }
        }
        return num1 - num2;
    }
}
