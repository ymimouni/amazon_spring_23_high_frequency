from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = data.count(1)

        left, right = 1, ones

        # Number of 1's in the subarray.
        sub_ones = sum(1 for i in range(ones) if data[i] == 1)
        max_sub_ones = sub_ones

        while right < len(data):
            sub_ones += -data[left - 1] + data[right]
            max_sub_ones = max(max_sub_ones, sub_ones)
            left += 1
            right += 1

        return ones - max_sub_ones
