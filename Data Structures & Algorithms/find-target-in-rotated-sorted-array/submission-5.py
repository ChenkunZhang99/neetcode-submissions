class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_index = self.findMin(nums)
        left = 0
        right = 0
        if nums[-1] >= target:
            left= min_index
            right = len(nums)-1
        else:
            right = min_index-1
        while left <= right:
            mid= (right - left )//2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return -1

    def findMin(self, nums):
        left , right = 0, len(nums)-1
        while left < right:
            mid = (right - left ) // 2 + left
            if nums[mid] > nums[right] : 
                left = mid + 1
            else : 
                right = mid
        return left