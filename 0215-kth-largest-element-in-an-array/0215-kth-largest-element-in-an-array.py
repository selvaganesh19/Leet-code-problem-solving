class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k

        l, r = 0, len(nums) - 1

        while l <= r:
            pivot = nums[(l + r) // 2]

            low = l
            i = l
            high = r

            while i <= high:
                if nums[i] < pivot:
                    nums[low], nums[i] = nums[i], nums[low]
                    low += 1
                    i += 1

                elif nums[i] > pivot:
                    nums[i], nums[high] = nums[high], nums[i]
                    high -= 1

                else:
                    i += 1

            if target < low:
                r = low - 1

            elif target > high:
                l = high + 1

            else:
                return nums[target]