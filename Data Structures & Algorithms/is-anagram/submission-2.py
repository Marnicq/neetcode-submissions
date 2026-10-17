class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_count_s = {}
        for i in s:
            char_count_s[i] = char_count_s.get(i, 0) + 1
        for i in t:
            char_count_s[i] = char_count_s.get(i, 0) - 1
        
        #return all(v == 0 for v in char_count_s.values())
        for v in char_count_s.values():
            if v != 0:
                return False
        return True