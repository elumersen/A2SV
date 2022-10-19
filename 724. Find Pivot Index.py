class Solution(object):
    def pivotIndex(self, nums):
        prev_sum=0
        totalSum = sum(nums)
        for i in range(len(nums)):
            if prev_sum==(totalSum-nums[i]-prev_sum):
                return i
            prev_sum=prev_sum+nums[i]
        return -1
        """
        :type nums: List[int]
        :rtype: int
        """
