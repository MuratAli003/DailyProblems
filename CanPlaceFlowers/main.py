"""
Bazı arazilerin ekildiği ve bazılarının ekilmediği uzun bir çiçek tarlığınız var. Ancak, bitişik arazilere çiçek ekilemez.

0'lar ve 1'ler içeren bir tamsayı dizisi çiçek yatağı göz önüne alındığında, burada 0 boş, 1 boş değil anlamına gelir ve bir tamsayı n, bitişik çiçek yok kuralını ihlal etmeden çiçek yatağına n yeni çiçek ekilebilirse doğru ve aksi takdirde yanlış döndürür.
-------------------------------------------------------------------------------------------------
Örnek 1:

Giriş: çiçeklik = [1,0,0,0,1], n = 1

Çıktı: doğru
------------------------------------------------------------------------------------------------
Örnek 2:

Giriş: çiçeklik = [1,0,0,0,1], n = 2

Çıktı: yanlış
"""
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        
        control = 1
        for i in range(0,len(flowerbed)):

            if flowerbed[i] == 0:
                control += 1
            else:
                control = 0
            if i == len(flowerbed)-1 and flowerbed[i] == 0 and control == 2:
                n-=1
            if control == 3:
                control = 1
                n -=1
        
        return True if n <= 0 else False