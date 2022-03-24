class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        d = {}
        maxLength = 0

        while right < len(s):
            if s[right] in d:
                left = max(d[s[right]] + 1, left)
                d[s[right]] = right

            d[s[right]] = right
            maxLength = max(maxLength, right - left + 1)
            right += 1

        return maxLength
