class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  #Liste sortieren brauch O(n log n)
        
        for i in range(len(nums) - 2):
            # Optimierung & Vermeidung von Duplikaten für die erste Zahl
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # Summe ist zu klein, brauche größere Zahl
                elif total > 0:
                    right -= 1 # Summe ist zu groß, brauche kleinere Zahl
                else:
                    # Treffer!
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Duplikate für das zweite und dritte Element überspringen
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
        return res