class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for wort in strs:
            länge = len(wort)
            out += str(länge) + "#" + wort
        return out


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            laenge = int(s[i:j])
            
            wort = s[j + 1 : j + 1 + laenge]
            res.append(wort)
            
            i = j + 1 + laenge
            
        return res
