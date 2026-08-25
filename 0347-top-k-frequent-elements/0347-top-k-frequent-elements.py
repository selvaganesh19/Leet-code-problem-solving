class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)

        for i in range(len(nums)): m[nums[i]]+=1

        heap = []

        for f,i in m.items():
            heapq.heappush(heap,(i,f))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [nums for _,nums in heap]