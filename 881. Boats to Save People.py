class Solution(object):
    def numRescueBoats(self, people, limit):
        left=0
        right=len(people)-1
        number_of_boats=0
        people.sort()
        while right>=left:
            if left==right:
                number_of_boats+=1
                break
            if people[left]<=limit-people[right]:
                left+=1
                right-=1
                number_of_boats+=1
                continue
            else:
                right-=1
                number_of_boats+=1
        return number_of_boats
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
