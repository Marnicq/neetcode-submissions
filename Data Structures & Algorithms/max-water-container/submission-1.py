class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        
        while left < right:
            width = right - left
            
            # 2. Die Höhe wird durch die kleinere der beiden Wände begrenzt
            current_height = min(heights[left], heights[right])
            area = width * current_height
            
            # 4. Maximale Fläche aktualisieren, falls die aktuelle größer ist
            max_area = max(max_area, area)
            
            # 5. Den Zeiger mit der kleineren Wand nach innen bewegen
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_area