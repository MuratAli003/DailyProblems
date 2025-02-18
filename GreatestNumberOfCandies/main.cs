"""
N şekerli çocuklar var. Size bir tamsayı dizisi şekerleri verilir, burada her bir şeker[i] çocuğun sahip olduğu şeker sayısını temsil eder ve sahip olduğunuz fazladan şeker sayısını gösteren bir tamsayı ekstra şekerler.

N uzunluğunda bir boolean dizi sonucu döndürün, burada sonuç[i] doğrudur, eğer ith çocuğa tüm ekstraCandies'i verdikten sonra, tüm çocuklar arasında en fazla sayıda şekere sahip olacaklarsa veya aksi takdirde yanlıştır.

Birden fazla çocuğun en fazla sayıda şekere sahip olabileceğini unutmayın.
---------------------------------------------------------------------------
Örnek 1:

Giriş: şekerler = [2,3,5,1,3], ekstra Şekerler = 3

Çıktı: [doğru, doğru, doğru, yanlış, doğru]

Açıklama: Tüm ekstraCandies'i verirseniz:

- Çocuk 1, çocuklar arasında en iyisi olan 2 + 3 = 5 şekere sahip olacaklar.

- Çocuk 2, çocuklar arasında en iyisi olan 3 + 3 = 6 şekere sahip olacaklar.

- Çocuk 3, çocuklar arasında en iyisi olan 5 + 3 = 8 şekere sahip olacaklar.

- Çocuk 4, 1 + 3 = 4 şekerleri olacak, ki bu çocuklar arasında en iyisi değil.

- Çocuk 5, çocuklar arasında en iyisi olan 3 + 3 = 6 şekere sahip olacaklar.
"""

public IList<bool> KidsWithCandies(int[] candies, int extraCandies) {
        
    List<bool> control = new List<bool>();
    int max = candies.Max();

    foreach (int candy in candies)
    {
        if (candy + extraCandies >= max)
        {
            control.Add(true);
        }
        else
        {
            control.Add(false);
        }
    }

    return control;
}