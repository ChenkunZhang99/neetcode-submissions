class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uni = set(nums)
        if not nums:
            return 0
        length = 1
        max_length = 1
        for num in uni:
            if num -1 in uni:
                continue
            temp = num
            while True:
                if temp + 1 in uni:
                    temp += 1
                    length += 1
                else:
                    break
            max_length = max (max_length, length)
            length = 1

        return max_length
        