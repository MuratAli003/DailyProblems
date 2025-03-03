"""
Yalnızca iki yığın kullanarak ilk giren ilk çıkar (FIFO) kuyruğu uygulayın. Uygulanan kuyruk, normal bir kuyruğun tüm işlevlerini desteklemelidir (push, peek, pop ve empty).

MyQueue sınıfını uygulayın:

* Void push(int x) x öğesini kuyruğun arkasına iter.

* Int pop() Öğeyi kuyruğun önünden kaldırır ve döndürür.
 
* Int peek() Kuyruğun önündeki öğeyi döndürür.

* Boolean empty() Kuyruk boşsa true, aksi takdirde false döndürür.

Notlar:

Bir yığının yalnızca standart işlemlerini kullanmanız gerekir, bu da yalnızca yukarı it, yukarıdan göz at/aç, boyut ve boş işlemlerin geçerli olduğu anlamına gelir.

Dilinize bağlı olarak, yığın yerel olarak desteklenmeyebilir. Yalnızca bir yığının standart işlemlerini kullandığınız sürece bir liste veya sıra (çift uçlu kuyruk) kullanarak bir yığını simüle edebilirsiniz.
"""
class MyQueue(object):

    def __init__(self):
        
        self.queue = []

    def push(self, x):
        
        self.queue.insert(0,x)
        

    def pop(self):
        
        return self.queue.pop()
        
        
        

    def peek(self):
        
        return self.queue[len(self.queue)-1]
        

    def empty(self):
        
        return len(self.queue) == 0
        
