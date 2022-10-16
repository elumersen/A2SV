class Solution(object):
    def maxArea(self, height):
        maxArea = 0
        right = len(height) - 1
        left = 0
        while(left < right):
            maxArea = max(maxArea, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                right-=1
                left+=1
        return maxArea
        """
        :type height: List[int]
        :rtype: int
        """
