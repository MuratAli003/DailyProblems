"""
Size yıldızları içeren bir dize s verilir *.

Bir operasyonda şunları yapabilirsiniz:

S'de bir yıldız seçin.

Solundaki en yakın yıldız olmayan karakteri kaldırın ve yıldızın kendisini kaldırın.

Tüm yıldızlar kaldırıldıktan sonra dizeyi döndürün.
-------------------------------------------------------------------------
Örnek 1:

Giriş: s = "leet**cod*e"

Çıktı: "lecoe"

Açıklama: Kaldırmaları soldan sağa doğru gerçekleştirme:

- 1. yıldıza en yakın karakter "leet**cod*e"deki 't'dir. s "lee*cod*e" olur.

- 2. yıldıza en yakın karakter "lee*cod*e"deki 'e'dir. s "lecod*e" olur.

- 3. yıldıza en yakın karakter "lecod*e"deki 'd'dir. s "lecoe" olur.

Artık yıldız yok, bu yüzden "lecoe" olarak geri dönüyoruz.
"""

public class Solution {
    public string RemoveStars(string s) {
        
        StringBuilder output = new StringBuilder();

            int i = 0;
            while (i < s.Length)
            {
                if (s[i] == '*')
                {
                    output.Remove(output.Length - 1, 1);
                    i++;
                }
                else
                {
                    output.Append(s[i]);
                    i++;
                }
            }

            return output.ToString();
    }
}