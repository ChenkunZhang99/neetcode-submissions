class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_no_space = "".join(c for c in s if c.isalnum()).lower()
        left = 0
        right = len(s_no_space) -1
        while left < right:
            if s_no_space[left] == s_no_space[right]:
                right -= 1
                left += 1
            else:
                return False
        return True