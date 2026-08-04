class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        w = sum(nums[:k])

        b = w

        for i in range(k, len(nums)):
            w+=nums[i] - nums[i-k]
            b = max(b,w)

        return b/k