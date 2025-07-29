# leetcode 217: Contains Duplicate
# Input: nums = [1,2,3,1]
# Output: true

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False

nums = [1, 2, 3, 1]
test = Solution()
print(test.hasDuplicate(nums))
