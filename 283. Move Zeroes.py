class Solution(object):
    def moveZeroes(self, nums):
        n= len(nums)
        right=0
        left=0
        if n==0 or n==1:
            return nums
        while right<n:
            if nums[right]!=0:
                nums[left], nums[right]= nums[right], nums[left]
                right+=1
                left+=1
            else:
                right+=1
        return nums
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
