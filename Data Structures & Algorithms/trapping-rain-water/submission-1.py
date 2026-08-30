
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0                    # 左指针，从最左边开始
        right = len(height) - 1     # 右指针，从最右边开始
        left_max = 0                # 记录"左指针走过的路径上，见过的最高的墙"
        right_max = 0               # 记录"右指针走过的路径上，见过的最高的墙"
        total_water = 0             # 累计总共能存的水量

        while left < right:
            # 第一步：比较两个指针当前指向的高度，决定处理哪一边
            if height[left] < height[right]:
                # 左边比较矮，说明：右边(从right到数组末尾)已知至少有一堵墙(height[right])
                # 比左边当前的高度更高，所以"left这个位置的水位"必然是被左边限制的，
                # 不需要知道右边具体多高，处理左边就是安全、准确的

                # 第二步：更新left_max —— 如果当前这根柱子比之前见过的都高，就更新纪录
                left_max = max(left_max, height[left])

                # 第三步：计算这个位置能存多少水
                # 水位由left_max决定(因为已经确定右边比left_max更高)
                # 减去这根柱子自己的高度，就是这个位置能存的水
                # 如果left_max就是height[left]本身(刚更新过)，这里会算出0，
                # 说明这根柱子本身就是"新的最高点"，存不了水，这是合理的
                total_water += left_max - height[left]

                # 第四步：左指针右移，处理下一个位置
                left += 1

            else:
                # 右边比较矮（或者两边相等，相等时移动哪边都一样，这里统一走这个分支）
                # 同理，右边的水位由right_max决定

                # 更新right_max
                right_max = max(right_max, height[right])

                # 计算这个位置能存多少水
                total_water += right_max - height[right]

                # 右指针左移
                right -= 1

        return total_water