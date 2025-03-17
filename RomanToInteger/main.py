"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.

------------------------------------------------------------
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

"""
class Solution(object):
    def romanToInt(self, s):
        
        dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        result = 0

        for i in range(0,len(s)-1):

            if dict[s[i]] < dict[s[i+1]]:
                result -= dict[s[i]]
            else:
                result += dict[s[i]]

        return result + dict[s[-1]]