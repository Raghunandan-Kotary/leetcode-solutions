class Solution(object):
    def productExceptSelf(self, n):
        answer = [1] * len(n)

        left = 1
        for i in range(len(n)):
            answer[i] = left
            left = left * n[i]

        right = 1
        for i in range(len(n) - 1, -1, -1):
            answer[i] = answer[i] * right
            right = right * n[i]

        return answer