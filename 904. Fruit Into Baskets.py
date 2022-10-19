class Solution(object):
    def totalFruit(self, fruits):
        left=0
        right=0
        max_length=0
        fruit={}
        # if len(fruits)==0:
        #     return 0
        # elif len(fruits)==1:
            # return 1
        while right < len(fruits):
            fruit[fruits[right]]=right
            if len(fruit) >= 3:
                least = min(fruit.values())
                del fruit[fruits[least]]
                left = least+1
            max_length = max(max_length, right-left+1)
            right+=1
        return max_length
        """
        :type fruits: List[int]
        :rtype: int
        """
