class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        found_word = False # Flag to indicate if we have started counting a word

        # Iterate backwards through the string
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                found_word = True 
                length += 1       
            elif found_word: 
                return length

        return length