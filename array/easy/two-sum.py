# leetcode 1: Two Sum
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            remainder = target - num
            if remainder not in hashmap:
                hashmap[num] = idx
            else:
                return [hashmap[remainder], idx]

test = Solution()

nums = [2, 7, 11, 15]
target = 9
# ans [0, 1]

print(test.twoSum(nums, target))

nums = [3, 2, 4]
target = 6
# ans [1, 2]

print(test.twoSum(nums, target))
