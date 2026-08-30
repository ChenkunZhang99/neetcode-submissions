class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()   # 存的是下标，不是值
        result = []

        for right in range(len(nums)):
            # 第一步：踢出队尾所有"比当前值小或相等"的下标
            # 因为它们以后不可能再是最大值了，没用了
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            # 第二步：把当前下标加入队尾
            dq.append(right)

            # 第三步：检查队首是否已经过期（滑出窗口范围）
            # 窗口的左边界是 right - k + 1
            left_bound = right - k + 1
            if dq[0] < left_bound:
                dq.popleft()

            # 第四步：只有当窗口大小已经达到k的时候，才开始记录答案
            if right >= k - 1:
                result.append(nums[dq[0]])

        return result