class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    bracket_map = {")": "(", "}": "{", "]": "["}

    for char in s:
      # Wenn das Zeichen eine schließende Klammer ist
      if char in bracket_map:
        # Nimm das oberste Element vom Stack (oder einen Dummy-Wert, falls leer)
        top_element = stack.pop() if stack else "#"

        # Prüft, ob das oberste Element zur schließenden Klammer passt
        if bracket_map[char] != top_element:
          return False
      else:
        # Wenn es eine öffnende Klammer ist, packe sie auf den Stack
        stack.append(char)

    # Am Ende ist der String nur gültig, wenn der Stack komplett leer ist
    return not stack