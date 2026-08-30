class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}   # 记录每个字符最近一次出现的位置
        left = 0
        max_len = 0

        for right in range(len(s)):
            char = s[right]

            # 如果这个字符出现过，且上次出现的位置还在当前窗口内，才移动left
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

            # 不管上面有没有触发，都要更新这个字符的最新位置
            char_index[char] = right

            # 用当前窗口长度，更新最大长度
            current_len = right - left + 1
            max_len = max(max_len, current_len)

        return max_len
            

