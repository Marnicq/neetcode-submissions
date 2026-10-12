class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       seen = set()
       for s in range(len(nums)):
        if nums[s] in seen:
            return True
        seen.add(nums[s])
       return False

