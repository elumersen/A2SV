class Solution:
    def sortColors(self, nums: List[int]) -> None:
        size = len(nums)
        for i in range(size):
            for j in range(i, size):
                if nums[j]< nums [i]:
                    nums[j],nums[i]=nums[i],nums[j]
        """
        Do not return anything, modify nums in-place instead.
        """
