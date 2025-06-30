class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opened = ["(", "[", "{"]
        closed = [")","]","}"]
        stack = []

        if s == "" or s[0] in closed:
            return False

        for i in range(len(s)):
            if s[i] in opened:
                stack.append(s[i])
            elif s[i] in closed:
                if stack and stack[-1] == opened[closed.index(s[i])]:
                    stack.pop()
                else:
                    return False
            else:
                return False
            
            
        return len(stack) == 0