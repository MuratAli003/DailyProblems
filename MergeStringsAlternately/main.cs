"""
Size word1 ve word2 olmak üzere iki dize verilir. Word1 ile başlayarak harfleri dönüşümlü sırayla ekleyerek dizeleri birleştirin. Bir dize diğerinden daha uzunsa, ek harfleri birleştirilmiş dizenin sonuna ekleyin.

Birleştirilmiş dizeyi döndür.
---------------------------------------------------------------
Örnek 1:

Giriş: word1 = "abc", word2 = "pqr"

Çıktı: "apbqcr"
----------------------------------------------------------------
Örnek 2:

Giriş: word1 = "ab", word2 = "pqrs"

Çıktı: "apbqrs"
"""

public string MergeAlternately(string word1, string word2) {
    string output = "";

    if (word1.Length > word2.Length)
    {
        for (int i = 0; i < word1.Length; i++)
        {
            output += word1[i];
            if (i < word2.Length)
            {
                output += word2[i];
            }
        }
    }
    else
    {
        for (int i = 0; i < word2.Length; i++)
        {
            if (i < word1.Length)
            {
                output += word1[i];
            }

            output += word2[i];
        }
    }

    return output;
    }