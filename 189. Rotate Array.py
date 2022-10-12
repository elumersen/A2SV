class Solution(object):
    def rotate(self, nums, k):
        k=k%len(nums)
        last=nums[:len(nums)-k]
        # print(last)
        first=nums[-1:-k-1:-1]
        first= list(reversed(first))
        # print(first)
        nums[:]=first+last
        print(nums)
        print(nums)
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
