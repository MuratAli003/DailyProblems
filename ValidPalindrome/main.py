"""
    Tüm büyük harfleri küçük harflere dönüştürdükten ve alfasayısal olmayan tüm karakterleri kaldırdıktan sonra aynı şeyi ileri ve geri okursa, bir ifade bir palindromdur. Alfasayısal karakterler harfleri ve sayıları içerir.

    Bir dize s verildiğinde, palindrom ise true, aksi takdirde false döndürün.

    Example 1:

    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

"""

def isPalindrome(s):
        
        s = s.lower().replace(" ","")

        char = "~`!@#$%^&*()_-+=[{]}\|;:'\",<.>/?"

        for i in char:

            s = s.replace(i,"")
        
        return s == s[::-1]
