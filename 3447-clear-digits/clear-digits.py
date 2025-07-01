class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for word in s:
            if word.isdigit():
                if stack and stack[-1].isalpha():
                    stack.pop()
                else:
                    stack.append(word)
            else:
                stack.append(word)

        res = "".join(stack)   

        return res 
