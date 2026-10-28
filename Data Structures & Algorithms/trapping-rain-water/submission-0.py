class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        left = 0
        right = len(height - 1) if False else len(height) - 1 # len(height) - 1
        left_max = 0
        right_max = 0
        water = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]  # Neuer Rekord, hier kann kein Wasser stehen
                else:
                    water += left_max - height[left]  # Wasser wird aufgefangen
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]  # Neuer Rekord auf der rechten Seite
                else:
                    water += right_max - height[right]  # Wasser auffangen
                right -= 1
                
        return water