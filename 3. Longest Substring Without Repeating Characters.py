class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sub_string = ''
        max_len = 0
        for letter in s:
            if letter not in sub_string:
                sub_string+=letter
                # print(sub_string)
            else:
                sub_string = sub_string[sub_string.index(letter) + 1:] + letter 
            max_len= max(max_len, len(sub_string))
        return max_len

        """
        :type s: str
        :rtype: int
        """
