class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        l=len(s)

        while i<l and s[i]==" ":
            i=i+1
        sign=1
        if i<l and s[i]=="-":
            sign= -1
            i+=1
        elif i<l and s[i]=="+":
            i+=1
        
        res=0
        while i<l and s[i].isdigit():
            res=res*10 + int(s[i])
            i=i+1
        res=res*sign
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if res>INT_MAX:
            res=INT_MAX
        if res<INT_MIN:
            res=INT_MIN
        return res