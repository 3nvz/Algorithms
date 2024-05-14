# 434. Number of Segments in a String

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        number = len(words)
        return number