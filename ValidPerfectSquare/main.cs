
"""
Pozitif bir tamsayı num verildiğinde, num mükemmel bir kare ise true veya aksi takdirde false döndürün.

Mükemmel bir kare, bir tam sayının karesi olan bir tam sayıdır. Başka bir deyişle, kendisiyle bir tam sayının ürünüdür.

Sqrt gibi herhangi bir yerleşik kitaplık işlevi kullanmamalısınız.

--------------------------------------------------------------------------------------
Örnek 1:

Giriş: sayı = 16

Çıktı: doğru

Açıklama: Doğru döndürüyoruz çünkü 4 * 4 = 16 ve 4 bir tam sayıdır.

--------------------------------------------------------------------------------------
Örnek 2:

Giriş: sayı = 14

Çıktı: yanlış

Açıklama: Yanlış döndürüyoruz çünkü 3.742 * 3.742 = 14 ve 3.742 tamsayı değildir.

"""

public bool IsPerfectSquare(int num)
{           
    long left = 0;
    long right = num;

    while (left <= right)
    {
        long mid = (left + right) / 2;

        if ((mid * mid) == num)
        {
            return true; 
        }
        
        if (mid * mid > num)
        {
            right = mid - 1; 
        }
        else
        {
            left = mid + 1; 
        }
    }
    return false;
}