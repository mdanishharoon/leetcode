class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        iter thru array
        
        
        """
        l = len(nums)

        left = [1] * l
        right = [1] * l

        res = [1] * l

        for i in range(1,l):
            left[i] = nums[i-1] * left[i-1]
        
        for i in range(l-2,-1,-1):
            right[i] = nums[i+1] * right[i+1]        
        
        for i in range(l):
            res[i] = left[i] * right[i]

        return res
        
    def main(self):
        print(self.productExceptSelf([1,2,3,4]))

Solution().main()
