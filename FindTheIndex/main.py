"""
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
--------------------------------------------------------
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 
"""
class Solution(object):
    def strStr(self, haystack, needle):
        
        for i in range(0,len(haystack)):
            
            if haystack[i:i+len(needle)] == needle:
                return i 
        
        return -1