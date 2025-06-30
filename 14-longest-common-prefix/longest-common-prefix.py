class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        parts = []

        for i in range(len(min(strs, key=len))):
            comp = strs[0][i]
            for word in strs:
                if word[i] != comp:
                    return "".join(parts)
            parts.append(comp)

        return "".join(parts)    



        