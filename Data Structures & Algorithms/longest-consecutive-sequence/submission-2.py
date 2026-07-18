from collections import Counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
#        nums = list(set(sorted(nums)))
#        counterDict = {}
#        print("NUMS ", nums)
#        for i in range(len(nums) - 1):
#            if nums[i+1] - nums[i] == 1:
#                counterDict[nums[i]] = [nums[i] for i in range(i,len(nums))]
#        print(counterDict)
        numSet = set(nums)
        longest = 0

        for n in nums:
            # Check if its a starting
            if (n-1) not in numSet:
                length = 0
                while (n+ length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest

