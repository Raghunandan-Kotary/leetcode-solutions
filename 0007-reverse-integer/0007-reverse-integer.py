import math

class Solution(object):
    def reverse(self, x):
        MIN = -2147483648
        MAX = 2147483647

        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(float(x) / 10)
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0

            if res < int(MIN / 10.0) or (res == int(MIN / 10.0) and digit < int(math.fmod(MIN, 10))):
                return 0

            res = (res * 10) + digit

        return res