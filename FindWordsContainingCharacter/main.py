"""
Size 0 dizili bir dize dizisi ve bir x karakteri verilir.

X karakterini içeren kelimeleri temsil eden bir dizi dizin döndürün.

Döndürülen dizinin herhangi bir sırada olabileceğini unutmayın.
---------------------------------------------------------------------
Örnek 1:

Giriş: kelimeler = ["leet","code"], x = "e"

Çıktı: [0,1]

Açıklama: "e" her iki kelimede de bulunur: "leet" ve "code". Bu nedenle, 0 ve 1 endekslerini döndürüyoruz.
"""

class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        
        wordIndex = []

        for index,word in enumerate(words):

            if x in word:
                wordIndex.append(index)

        return wordIndex 