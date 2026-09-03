class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        sl = len(s)
        freq = {}
        maxFreq = 0
        ans = 0

        while r < sl:
            freq[s[r]] = freq.get(s[r], 0) +1
            wl = r - l +1            

            maxFreq = max(freq.values())
            
            if (r - l +1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1

            ans = max(ans, r - l +1)
            r += 1

        return ans