class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0)+1
        #dann jetzt Keys sortieren
        sorted_keys = sorted(counts, key=counts.get, reverse=True)[:k]
        return sorted_keys
        