class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        neu = sorted(set(nums))
        counts = 1
        glob = 1
        for i in range(len(neu) - 1):
            if neu[i+1] == neu[i]+ 1:
                counts += 1
            else: 
                counts = 1

            if counts > glob:
                glob = counts
        return glob

        