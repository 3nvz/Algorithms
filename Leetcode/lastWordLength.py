# 58. Length of Last Word
# Beats 97%

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        last = len(words[-1])
        return last