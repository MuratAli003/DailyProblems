"""
Bir dizeyi 32 bit işaretli bir tamsayıya dönüştüren myAtoi(string s) işlevini uygulayın.

myAtoi(string s) algoritması aşağıdaki gibidir:

Boşluk: Öndeki herhangi bir boşluk (" ") dikkate almayın.

İşaretlilik: Bir sonraki karakterin '-' veya '+' olup olmadığını kontrol ederek işareti belirleyin, ikisi de mevcutsa pozitiflik varsayar.

Dönüşüm: Rakamsız bir karakterle karşılaşılana veya dizenin sonuna ulaşılana kadar öndeki sıfırları atlayarak tam sayıyı okuyun. Hiçbir rakam okunmadıysa, sonuç 0'dır.

Yuvarlama: Tamsayı 32 bit işaretli tamsayı aralığının [-231, 231 - 1] dışındaysa, aralıkta kalmak için tam sayıyı yuvarlayın. Özellikle, -231'den küçük tam sayılar -231'e yuvarlanmalı ve 231 - 1'den büyük tam sayılar 231 - 1'e yuvarlanmalıdır.

Tam sayıyı nihai sonuç olarak döndürün.
------------------------------------------------------------------------------------------

Örnek 1:

Giriş: s = "42"

Çıktı: 42

Açıklama:

Altı çizili karakterler okunan karakterlerdir ve kare mevcut okuyucu konumudur.

Adım 1: "42" (önde boşluk olmadığı için karakter okunmuyor)

^

Adım 2: "42" (ne '-' ne de '+' olduğu için karakter okunmadı)

^

Adım 3: "42" ("42" okunur)

^
------------------------------------------------------------------------------------------
Örnek 2:

Giriş: s = "20000000000000000000"

Çıktı: 2147483647

Açıklama:

Adım 1: "20000000000000000000" Integer değer aralığını aştığı için Integer max genişiğini alabilir
----------------------------------------------------------------------------------------
Örnek 3:

Giriş: s = "1337c0d3"

Çıktı: 1337

Açıklama:

Adım 1: "1337c0d3" (önde boşluk olmadığı için karakter okunmuyor)

^

Adım 2: "1337c0d3" (ne '-' ne de '+' olduğu için karakter okunmadı)

^

Adım 3: "1337c0d3" ("1337" okunur; bir sonraki karakter rakam olmadığı için okuma durur)
"""





public class Solution {
    public int MyAtoi(string s) {
        
        string a = "";

        for (int i = 0; i < s.Length; i++)
        {

            if (s[i] == '-')
            {
                if (a.Length != 0)
                {
                    break;
                }
                else
                {
                    a += s[i];
                }
            }

            else if (s[i] == '+')
            {
                if (a.Length != 0)
                {
                    break;
                }
                else
                {
                    a += s[i];
                }
            }

            else if (char.IsDigit(s[i]))
            {
                a += s[i];
            }

            else if(s[i] == ' ' && a.Length == 0){
                continue;
            }

            else
            {
                break;
            }
        }

        try
        {
            int result = Convert.ToInt32(a);
            return result;
        }
        catch (OverflowException e)
        {

            if(a[0] == '-'){

                return Int32.MinValue;
            }
            else{

                return Int32.MaxValue;

            }
        }
        catch (Exception e)
        {
            return 0;
        }
             
    }
}