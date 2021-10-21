class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s.isspace():
            return 0
        words = s.split()
        if words[-1].isalpha():
            return len(words[-1])
        else:
            return 0
