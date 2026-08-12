class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expandaroundcenter(s,left,right):
            max_len=0
            sub_str=""

            while left>=0 and right<len(s) and s[left]==s[right]:
                curr_length=right-left+1
                if curr_length>max_len:
                    max_len=curr_length
                    sub_str=s[left:right+1]
                left-=1
                right+=1
            return sub_str
        result=""
        for i in range(len(s)):
            odd=expandaroundcenter(s,i,i)
            even=expandaroundcenter(s,i,i+1)
            if len(odd)>len(result):
                result=odd
            if len(even)>len(result):
                result=even
        return result