class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        for i in range (len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                pre_res= prefix[i-1] * nums[i-1]
                prefix.append(pre_res)
        for i in range (len(nums)-1,-1,-1):
            if i == len(nums)-1:
                suffix.append(1)
            else:
                res = suffix[-1] * nums[i + 1]
                suffix.append(res)
        suffix.reverse()
        output = []
        for i in range (len(nums)):
            output.append(prefix[i]*suffix[i])
        return output