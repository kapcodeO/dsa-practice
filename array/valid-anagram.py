# leetcode 242: Valid Anagram
# Input: s = "anagram", t = "nagaram"
# Output: true

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter_s, counter_t = {}, {}

        # store the counts of s
        for item in s:
            if item not in counter_s:
                counter_s[item] = 1
            else:
                counter_s[item] += 1

        # store the counts of t
        for item in t:
            if item not in counter_t:
                counter_t[item] = 1
            else:
                counter_t[item] += 1

        return counter_s == counter_t

test = Solution()

s = "anagram"
t = "nagaram"

print(test.isAnagram(s, t))

s = "rat"
t = "car"

print(test.isAnagram(s, t))
            
