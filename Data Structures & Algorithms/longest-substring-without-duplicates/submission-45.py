class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq_dict = {}
       
        l = 0
        max_length = 1
        for r in range(len(s)):
            
            if s[r] in freq_dict:
                max_length = max(max_length, freq_dict[s[r-1]] - l + 1)
                l = r

            freq_dict[s[r]] = r

        return max_length