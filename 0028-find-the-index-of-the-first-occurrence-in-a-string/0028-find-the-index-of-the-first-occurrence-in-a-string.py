class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        limit = len(haystack) - len(needle) + 1

        for i in range(limit):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1