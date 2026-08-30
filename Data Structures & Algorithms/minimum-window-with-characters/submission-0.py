class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        # 第一步：统计t里每个字符需要多少个
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        need_count = len(need)   # t里一共有多少种不同的字符，需要全部被满足

        window_count = {}   # 记录当前窗口内，每个字符出现的次数
        have = 0             # 记录当前窗口里，已经有多少种字符"数量达标"了

        result = ""
        result_len = float("inf")   # 用无穷大初始化，方便后面找"更短"的答案

        left = 0
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            # 如果这个字符是t需要的，且数量刚好达到需求，have+1
            if char in need and window_count[char] == need[char]:
                have += 1

            # 当窗口已经满足所有字符需求时，尝试收缩left，寻找更短的窗口
            while have == need_count:
                # 记录/更新最优答案
                if (right - left + 1) < result_len:
                    result = s[left:right+1]
                    result_len = right - left + 1

                # 尝试移除left这个字符，收缩窗口
                left_char = s[left]
                window_count[left_char] -= 1

                # 如果移除后，这个字符的数量跌破了需求，have要减1
                if left_char in need and window_count[left_char] < need[left_char]:
                    have -= 1

                left += 1

        return result