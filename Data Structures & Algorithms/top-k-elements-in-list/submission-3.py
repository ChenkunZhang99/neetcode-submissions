class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = 1 + freqs.get(num,0) 
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freqs.items():
            buckets[freq].append(num)
        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for  num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        return res

