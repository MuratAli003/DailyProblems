"""
İmzalı bir 32 bit tam sayı x verildiğinde, x'i basamakları ters çevrilmiş olarak döndürün. X'i tersine çevirmek, değerin imzalı 32 bit tamsayı aralığının [-231, 231 - 1] dışına çıkmasına neden olursa, 0 döndürün.

Ortamın 64 bit tamsayıları (imzalı veya imzasız) depolamanıza izin vermediğini varsayalım.
--------------------------------------
Örnek 1:

Giriş: x = 123

Çıktı: 321
---------------------------------------
Örnek 2:

Giriş: x = -123

Çıktı: -321
----------------------------------------
Örnek 3:

Giriş: x = 120

Çıktı: 21
"""


public static int Reverse(int x)
{

            string a = Convert.ToString(x);
            string b = "";

            bool isNegative = false;
            for (int i = a.Length-1; i >= 0; i--)
            {
                if(a[i] == '-'){
                    isNegative = true;
                }
                else if(a[i] == '+'){
                    continue;
                }
                else{
                    b += a[i];
                }
            }

            try
            {
                if(isNegative){
                    return Convert.ToInt32(b) * (-1);
                }
                else{
                    return Convert.ToInt32(b);
                }
            }
            catch (Exception e)
            {
                return 0;
            }
}      