class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq_dict = {}
       
        l = 0
        max_length = 0
        for r in range(len(s)):
            
            if s[r] in freq_dict:
                l = r
            max_length = max(max_length, r - l + 1)

            freq_dict[s[r]] = r

        return max_length