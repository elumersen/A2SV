class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        mySortedList = sorted(nums)
        result = []
#         print(mySortedList)
        my_dct= {}
        for i in range(len(mySortedList)):
                if mySortedList[i] not in my_dct:
                    my_dct[mySortedList[i]] = i 
#         print(my_dct)
        for i in nums:
                result.append(my_dct[i])
        return result
