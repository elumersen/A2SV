class Solution(object):
    def numberOfSubarrays(self, nums, k):
        oddNums = []
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                oddNums.append(i)
        left = 0
        right = k - 1
        i = 0
        count = 0
        while right < len(oddNums):
            if right == len(oddNums) - 1:
                j = len(nums) - 1
            else:
                j = oddNums[right + 1] - 1
            count = count + (oddNums[left] - i + 1) * (j - oddNums[right] + 1)
            i = oddNums[left] + 1
            left = left + 1
            right = right + 1
        return count
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
