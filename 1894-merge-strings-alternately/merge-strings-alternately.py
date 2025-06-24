class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
           
        i = len(word1)
        j = len(word2)
        
        k=0
        l=0
        word3 = ""

        while k<i and l<j:
            word3 += word1[k]
            word3 += word2[l]
            k+=1
            l+=1
        
        while k<i:
            word3 += word1[k]
            k+=1
        
        while l<j:
            word3 += word2[l]
            l+=1

        return word3

        
            

        