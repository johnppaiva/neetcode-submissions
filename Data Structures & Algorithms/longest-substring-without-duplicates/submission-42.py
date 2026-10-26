class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        freq_dict = {}

        l = 0
        max_length = 0
        for r in range(len(s)):
            
            if s[r] in freq_dict:
                max_length = max(max_length, r - l)
                l = r
            freq_dict[s[r]] = r

        return max_length