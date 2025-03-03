"""
Yalnızca iki kuyruk kullanarak bir son giren ilk çıkar (LIFO) yığını uygulayın. Uygulanan yığın, normal bir yığının tüm işlevlerini (itme, üst, pop ve boş) desteklemelidir.

MyStack sınıfını uygulayın:

* Void push(int x) x öğesini yığının en üstüne iter.

* Int pop() Yığının üstündeki öğeyi kaldırır ve döndürür.

* Int top() Yığının üstündeki öğeyi döndürür.

* Boolean empty() Yığın boşsa true döndürür, aksi takdirde false döndürür.

Notlar:

Bir kuyruğun yalnızca standart işlemlerini kullanmalısınız, bu da yalnızca arkaya itme, önden peek/pop, boyut ve boş işlemlerin geçerli olduğu anlamına gelir.

Dilinize bağlı olarak, kuyruk yerel olarak desteklenmeyebilir. Yalnızca bir kuyruğun standart işlemlerini kullandığınız sürece bir liste veya deque (çift uçlu kuyruk) kullanarak bir sırayı simüle edebilirsiniz.
"""

class MyStack(object):

    def __init__(self):
        
        self.stack = deque()

    def push(self, x):
        
        self.stack.append(x)
        

    def pop(self):
        
        for i in range(0,len(self.stack)-1):

            self.stack.append(self.stack.popleft())
        return self.stack.popleft()

    def top(self):
        
        return self.stack[-1]
        

    def empty(self):
        
        return len(self.stack) == 0
        


