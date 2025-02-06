"""
İki dizi arr1 ve arr2 verildiğinde, arr2'nin elemanları farklıdır ve arr2'deki tüm öğeler de arr1'dedir.

Arr1 öğelerini, arr1'deki öğelerin göreceli sıralaması arr2'dekiyle aynı olacak şekilde sıralayın. Arr2'de görünmeyen öğeler arr1'in sonuna artan sırayla yerleştirilmelidir.

Örnek 1:

Giriş: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]

Çıktı: [2,2,2,1,4,3,3,9,6,7,19]

Örnek 2:

Giriş: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]

Çıktı: [22,28,8,6,17,44]
"""

def relativeSortArray(arr1, arr2):
        
    for i in arr2:

        arr1.remove(i)
        
    arr1.sort()

    for i in range(len(arr1)):

        if(arr1[i] in arr2):

            indx = arr2.index(arr1[i])
            arr2.insert(indx,arr1[i])
            
        else:

            arr2.append(arr1[i])

    return arr2
