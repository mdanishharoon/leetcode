class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
       """
        a = s.split(" ")
        a.reverse()
        cleaned_list = [s for s in a if s != ""]
        return " ".join(cleaned_list)
