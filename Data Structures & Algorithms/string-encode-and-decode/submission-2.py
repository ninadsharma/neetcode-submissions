class Solution:
    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        # get the length of each word and split the letters of each index
        for word in strs:
            length = len(word)                # get the length to iterate later
            encodedStr += str(length) + "#"   # add # to split the string later
            encodedStr += word                # add the word to the # and length
        return encodedStr
        
    def decode(self, s: str) -> List[str]:
        print(s) 
        decodedStr = []
        index = 0
        p1, p2 = 0, 0

        while p1 < len(s):
            p2 = p1
            while s[p2] != "#":
                p2 += 1
            length = int(s[p1:p2])
            decodedStr.append(s[p2 + 1: p2 + length + 1])

            p1 = p2 + length + 1
        return decodedStr



