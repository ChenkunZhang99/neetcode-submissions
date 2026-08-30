class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n_set = set()
        for i in nums:
            if i in n_set:
                return True
            n_set.add(i)
        return False 