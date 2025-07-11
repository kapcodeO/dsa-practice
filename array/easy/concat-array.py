# leetcode 1929: Concatenation of Array

# Input: nums = [22,21,20,1]
# Output: [22,21,20,1,22,21,20,1]

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

nums = [22,21,20,1]
test = Solution()
print(test.getConcatenation(nums))
