class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1]*n
        # durchlauf von links nach rechts
        prefix = 1
        for i in range(n):
            out[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1): #range(Start, Stopp, Schrittweite)
            out[i] *= postfix
            postfix *= nums[i]
        return out