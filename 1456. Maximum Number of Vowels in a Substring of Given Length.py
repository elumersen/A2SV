class Solution(object):
    def maxVowels(self, s, k):
        vowels='aeiou'
        num_of_vowels=0
        for i in range(k):
            if s[i] in vowels:
                num_of_vowels=num_of_vowels+1
        max_numOf_vowels=num_of_vowels
        for i in range(len(s)-k):
            if s[i] in vowels:
                num_of_vowels=num_of_vowels-1
            if s[i+k] in vowels:
                num_of_vowels=num_of_vowels+1
            max_numOf_vowels=max(max_numOf_vowels,num_of_vowels)
        return max_numOf_vowels
        """
        :type s: str
        :type k: int
        :rtype: int
        """
