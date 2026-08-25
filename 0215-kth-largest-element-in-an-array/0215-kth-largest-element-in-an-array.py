class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        count = 0
        arr = []
        for num in nums:
            if count==k:
                heapq.heappush(arr,num)
                temp = heapq.heappop(arr)
            else:
                heapq.heappush(arr,num)
                count+=1
        return arr[0]
        