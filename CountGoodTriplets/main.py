"""
Bir dizi tam sayı arr ve üç tam sayı a, b ve c verildiğinde. İyi üçüzlerin sayısını bulmalısın.

Aşağıdaki koşullar doğruysa bir üçlü (arr[i], arr[j], arr[k]) iyidir:

* 0 <= i < j < k < arr.length

* |arr[i] - arr[j]| <= a

* |arr[j] - arr[k]| <= b

* |arr[i] - arr[k]| <= c

Burada |x| x'in mutlak değerini belirtir.

İyi üçüzlerin sayısını döndürün.
-----------------------------------------------------------------------
Örnek 1:

Giriş: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3

Çıktı: 4

Açıklama: 4 iyi üçlü vardır: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

"""
class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        
        result = 0

        for index1,num1 in enumerate(arr[:len(arr)-2]):
            for index2,num2 in enumerate(arr[index1+1:len(arr)-1] , start = index1+1):
                if abs(num1 - num2) <= a:
                    for index3,num3 in enumerate(arr[index2+1:],start = index2+1):
                        if abs(num2 - num3) <= b and abs(num1 - num3) <= c:
                            result += 1
        
        return result
        