class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text= re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        chars = []
        for char in clean_text:
            chars.append(char)

        chars.reverse()  # Liste umdrehen
        reversed_text = "".join(chars)

        if clean_text == reversed_text:
            return True
        else:
            return False