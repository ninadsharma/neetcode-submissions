class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            sCharCount = {char: s.count(char) for char in set(s)}
            print(sCharCount)
            tCharCount = {char: t.count(char) for char in set(t)}
            print(tCharCount)
            return sCharCount == tCharCount
