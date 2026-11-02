class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        store = {}
        length = 0
        l = 0
        for r in range(len(s)):
            store[s[r]] = 1 + store.get(s[r],0)
            if ((r - l + 1) - max(store.values())) <= k:
                length = max(length,r - l + 1)
            else:
                pass

        return length