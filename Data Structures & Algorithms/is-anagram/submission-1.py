class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = [0] * 26
        for i in range(len(s)):
            index_s = ord(s[i]) - ord("a")
            counts[index_s] += 1
            index_t = ord(t[i]) - ord("a")
            counts[index_t] -= 1
        for i in range(len(counts)):
            if counts[i] != 0:
                return False
        return True