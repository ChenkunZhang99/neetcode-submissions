class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            # 跳过重复的first
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # 小优化：如果最小的数字都大于0，后面不可能凑出0了，直接结束
            if nums[i] > 0:
                break

            target_for_two = -nums[i]
            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target_for_two:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # 跳过重复的left值
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    # 跳过重复的right值
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif current_sum < target_for_two:
                    left += 1
                else:
                    right -= 1

        return result        