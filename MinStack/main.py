"""
Push, pop, top ve minimum öğeyi sabit zamanda almayı destekleyen bir yığın tasarlayın.

MinStack sınıfını uygulayın:

* MinStack() yığın nesnesini başlatır.

* Void push(int val) val öğesini yığına iter.

* Void pop() yığının üstündeki öğeyi kaldırır.

* Int top() yığının en üst öğesini alır.

* Int getMin() yığındaki minimum öğeyi alır.

Her işlev için O(1) zaman karmaşıklığına sahip bir çözüm uygulamanız gerekir.

"""

class MinStack(object):

    def __init__(self):
        
        self.list = []
        self.minList = []
        

    def push(self, val):
        
        self.list.append(val)
        self.minList.append(val if not self.minList else min(val,self.minList[-1]))
        

    def pop(self):
        
        self.list.pop()
        self.minList.pop()

    def top(self):
        
        return self.list[-1]
        

    def getMin(self):
       
        return self.minList[-1]

