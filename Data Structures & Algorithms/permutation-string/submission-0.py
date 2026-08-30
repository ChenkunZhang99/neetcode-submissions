class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        window_count = {}
        m = len(s1)

        for right in range(len(s2)):
            # 移入新字符
            window_count[s2[right]] = window_count.get(s2[right], 0) + 1

            # 如果窗口超过了固定长度m，需要移出最左边的字符
            if right >= m:
                left_char = s2[right - m]
                window_count[left_char] -= 1
                if window_count[left_char] == 0:
                    del window_count[left_char]

            # 检查窗口是否等于目标长度m，并且内容是否匹配
            if right >= m - 1 and window_count == s1_count:
                return True

        return False        