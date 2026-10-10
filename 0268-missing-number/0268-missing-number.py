class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        actual=sum(nums)
        expected=n*(n+1)//2

        return expected-actual