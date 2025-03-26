"""
Sadece '(', ')', '{', '}', '[' ve ']' karakterlerini içeren bir dize s verildiğinde, giriş dizesinin geçerli olup olmadığını belirleyin.

Bir giriş dizesi şu durumlarda geçerlidir:

Açık parantezler aynı tür parantezlerle kapatılmalıdır.

Açık parantezler doğru sırayla kapatılmalıdır.

Her yakın parantez aynı türden karşılık gelen bir açık paranteze sahiptir.
-----------------------------------------------------------------------------
Örnek 1:

Giriş: s = "()"

Çıktı: doğru
--------------------------------------------------------------------------------
Örnek 2:

Giriş: s = "()[]{}"

Çıktı: doğru
"""
class Solution(object):
    def isValid(self, s):
        
        chars = {
            "}" : "{",
            ")" : "(",
            "]" : "[" 
        }
        stack = []

        for i in s:

            if i == "{" or i == "[" or i == "(":

                stack.append(i)
                
            else:

                if len(stack) == 0 or stack.pop() != chars[i] :
                    return False
                 
        
        return len(stack) == 0

        