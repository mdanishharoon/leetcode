class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O','U' ]
        a = list(s)

        start = 0
        end = len(s)-1

        while (end>start):
            if a[start] in vowels:
                if a[end] in vowels:
                    a[start],a[end] = a[end], a[start]
                    start+=1
                    end-=1
                else:
                    end-=1 
            else:
                start+=1

        res = "".join(a)

        return res   
                    
            
            
"""
use two pointers
find first vowel in string and stop the  pointer there
iterate to next until u find the last vowel
"""
