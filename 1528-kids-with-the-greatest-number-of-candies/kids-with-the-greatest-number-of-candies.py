class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        max_candies = max(candies)
        res = []
        for kid in candies:
            if ((kid + extraCandies)>= max_candies):
                res.append(True)
            else:
                res.append(False)

        print(res)
        return res