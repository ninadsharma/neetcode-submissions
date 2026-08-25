class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Check for a letter and compare if its in a set of seen sequences
        i, j = 0, 0
        seenAt = {}

        n = len(s)
        longest = 0

        for j in range(n):
            if s[j] in seenAt:
                i = max( i, seenAt[s[j]] +1 )    

            seenAt[s[j]] = j
            longest = max( longest, j -i +1 )

        return longest

'''
        while j < n:
            if s[j] not in window:
                window.add(s[j])
                j = j + 1
                longest = max(j - i, longest)

            else:
                window.remove(s[i])
                i += 1

        return longest

'''