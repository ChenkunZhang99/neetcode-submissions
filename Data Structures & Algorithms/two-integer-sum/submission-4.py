class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i,k in enumerate(nums):
            index[k] = i
        
        for i , k in enumerate (nums):
            diff = target - k
            if diff in index and index[diff] != i : 
                return [i,index[diff]]
        return []
         