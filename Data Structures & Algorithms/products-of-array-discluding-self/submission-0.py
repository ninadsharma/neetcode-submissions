class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodToLeft, prodToRight, finalArray= [], [], []

        mulTemp = 1
        for i in range(len(nums)):  # Left Side Prod Loop
            if i == 0:
                prodToLeft.append(mulTemp)
                #print("MulTemp at Index => ",mulTemp, i)

            else:
                mulTemp = mulTemp * nums[i-1]
                prodToLeft.append(mulTemp)
                print("MulTemp at Index => ",mulTemp, i)
        #print("left Trailing products",prodToLeft)

        mulTemp = 1
        i = len(nums)-1
        while i >= 0:  # Right Side Prod Loop
            if i == len(nums) - 1:
                prodToRight.append(mulTemp)
                #print("RIGHT LOOP MulTemp at Index => ",mulTemp, i)
            else:
                mulTemp = mulTemp * nums[i+1]
                prodToRight.append(mulTemp)
                #print("RIGHT LOOP MulTemp at Index => ",mulTemp, i)

            i = i-1
        prodToRight.reverse()
        #print("RIGHT Trailing products",prodToRight)


        for i in range(len(nums)):
            finalArray.append(prodToLeft[i] * prodToRight[i])

        #print(finalArray)   

        return finalArray   

