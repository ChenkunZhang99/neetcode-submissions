class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}       # 记录当前窗口内，每个字符出现的次数
        left = 0
        max_len = 0
        max_count = 0    # 记录窗口内，出现次数最多的字符，出现了多少次

        for right in range(len(s)):
            char = s[right]
            count[char] = count.get(char, 0) + 1
            max_count = max(max_count, count[char])

            window_len = right - left + 1

            # 如果"需要替换的字符数"超过了k，说明窗口不合法，收缩left
            if window_len - max_count > k:
                left_char = s[left]
                count[left_char] -= 1
                left += 1

            # 用当前窗口长度更新最大长度
            max_len = max(max_len, right - left + 1)
        return max_len
