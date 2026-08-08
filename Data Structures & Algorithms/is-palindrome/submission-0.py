class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(s)
        s = "".join(letter for letter in s if letter.isalnum()).lower()

        print(s)

        # MAIN TWO POINTER
        i, j = 0, len(s) -1
        while (i<j):
            if (s[i] == s[j]):
                print("IF>>",s[i], s[j], s[i] == s[j])
                pass
            else:
                print("ELSE>>", s[i], s[j], s[i] == s[j])
                return False
            i += 1
            j -= 1
        return True





