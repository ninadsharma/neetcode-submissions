class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            sCharCount = {char: s.count(char) for char in set(s)}
            tCharCount = {char: t.count(char) for char in set(t)}
            return sCharCount == tCharCount
