class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Check for a letter and compare if its in a set of seen sequences
        i, j = 0, 0
        window = set()
        n = len(s)
        longest = 0

        while j < n:
            if s[j] not in window:
                window.add(s[j])
                j = j + 1
                longest = max(j - i, longest)

            else:
                window.remove(s[i])
                i += 1

        return longest

