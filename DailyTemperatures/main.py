"""
Bir dizi tamsayı sıcaklığının günlük sıcaklıkları temsil ettiği göz önüne alındığında, cevap[i], daha sıcak bir sıcaklık elde etmek için i. günden sonra beklemeniz gereken gün sayısı olacak şekilde bir dizi cevabı döndürün. Bunun mümkün olduğu gelecekte bir gün yoksa, bunun yerine cevabı [i] == 0 olarak tutun.
--------------------------------------------------------------------------
Örnek 1:

Giriş: sıcaklıklar = [73,74,75,71,69,72,76,73]

Çıktı: [1,1,4,2,1,1,0,0]
"""
class Solution(object):
    def dailyTemperatures(self, temperatures):
        
        result = [0] * len(temperatures)
        newStack = []

        for index,temperature in enumerate(temperatures):

            while newStack and temperature > newStack[-1][0]:

                stackTemperature ,stackIndex = newStack.pop()
                result[stackIndex] = index - stackIndex

            newStack.append([temperature,index]) 
        return result
        