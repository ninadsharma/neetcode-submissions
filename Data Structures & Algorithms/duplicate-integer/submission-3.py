class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupDict = {x: x for x in nums}
        return len(dupDict) != len(nums)




# 2nd 
# Two pointer = needs sorted array 
# [_,_,_,_]

# Hashset = Set {"":""}
