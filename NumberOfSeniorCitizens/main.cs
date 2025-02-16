"""
Size 0 dizinli bir dize ayrıntıları dizisi verilir. Her ayrıntı öğesi, uzunluğu 15 olan bir diziye sıkıştırılmış belirli bir yolcu hakkında bilgi sağlar. Sistem şu şekildedir:

İlk on karakter yolcuların telefon numaralarından oluşur.

Bir sonraki karakter, kişinin cinsiyetini belirtir.

Aşağıdaki iki karakter kişinin yaşını belirtmek için kullanılır.

Son iki karakter, o kişiye tahsis edilen koltuğu belirler.

Kesinlikle 60 yaşın üzerinde olan yolcu sayısını geri alın.
---------------------------------------------------------------------------
Örnek 1:

Giriş: ayrıntılar = ["7868190130M7522","5303914400F9211","9273338290F4010"]

Çıktı: 2

Açıklama: 0, 1 ve 2 endekslerindeki yolcuların yaşları 75, 92 ve 40'tır. Bu nedenle, 60 yaşın üzerindeki 2 kişi var.
"""
public class Solution {
    public int CountSeniors(string[] details) {
        
         int output = 0;

            foreach (string detail in details)
            {
                int age = Convert.ToInt32(detail.Substring(11, 2));
                if (age > 60)
                {
                    output++;
                }
            }

            return output;
    }
}