class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        numofzeros = 0
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                numofzeros += 1
            while numofzeros > k:  
                if nums[left] == 0:
                    numofzeros -= 1
                left += 1
            max_len = max(max_len, i - left + 1)
        return max_len
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
