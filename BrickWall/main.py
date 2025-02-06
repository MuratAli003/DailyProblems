"""
2 boyutlu dizi içerisinde verilmiş tuğlaları hayal edelim. Bu tuğlalar belirli uzunluklarla yerleştirilmiş.
Tuğlalar arasındaki boşluklardan geçilmeye çalışılmaktadır. En az tuğlayı kıracak şekilde mevcut olan geçidi geri döndürün. 

"""

def leastBricks(wall):
        
        """
        :type wall: List[List[int]]
        :rtype: int
        """
         
        dicts = {0:0}

        for i in wall:
            control = 0
            for index,j in enumerate(i):

                if index != len(i)-1:
                    control += j
                    if control in dicts.keys():

                        dicts[control] += 1 
                    else:
                        dicts[control] = 1

        result = len(wall) - max(dicts.values())
        return result
