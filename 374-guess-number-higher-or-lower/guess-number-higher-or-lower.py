# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        
        while start <= end:
            curr_guess = (start + end) // 2
            if(guess(curr_guess) == 0):
                return curr_guess
            elif(guess(curr_guess) == -1):
                end = curr_guess - 1
            else:
                start = curr_guess + 1
            

        return curr_guess
                