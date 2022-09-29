class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted = False
        finalArray=[]
        while not sorted:
            sorted = True
            for i in range(0, len(nums)-1):
                if nums[i]> nums[i+1]:
                    sorted = False
                    nums[i], nums[i+1] = nums[i+1], nums[i]
        for i in range(0, len(nums)):
            if nums[i]==target:
                finalArray.append(i)
        return finalArray
    

