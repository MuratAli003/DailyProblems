"""
Bir tam sayı n verildiğinde, ikinin gücüyse doğru döndürün. Aksi takdirde, yanlış döndürün.

Bir tam sayı n, n == 2^x olacak şekilde bir tam sayı x varsa, ikinin kuvvetidir.
"""
def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    
    while n > 1:
        if n % 2 != 0:
            return False
        n /= 2.0

    return n == 1
