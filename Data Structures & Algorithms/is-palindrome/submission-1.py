class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        s = "".join(letter for letter in s if letter.isalnum()).lower()

        # MAIN TWO POINTER
        i, j = 0, len(s) -1
        while (i<j):
            if (s[i] == s[j]):
                pass
            else:
                return False
            i += 1
            j -= 1
        return True





