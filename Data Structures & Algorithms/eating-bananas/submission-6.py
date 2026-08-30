class Solution:
    def helpfunc(self, piles: List[int], k:int ) -> int: # 计算需要多少小时
        hours = 0
        for i in piles:
            hours += ( i + k -1 ) // k
        return hours
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # max(piles) and sum(piles)
        max_k = max(piles)
        min_k = 1
        res = max_k
        while min_k <= max_k:
            mid_k = (max_k - min_k + 1) // 2 + min_k
            hours = self.helpfunc(piles,mid_k)
            if hours <= h: #如果等于h, 那么就说明k有减少的可能
                res = mid_k
                max_k = mid_k - 1 
            elif hours >h : # 说明规定时间内吃不完, 需要加大K
                min_k = mid_k + 1
        return res

        
