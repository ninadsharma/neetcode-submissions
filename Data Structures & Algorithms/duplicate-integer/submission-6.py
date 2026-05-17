class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupDict = {x: x for x in nums}
        return len(dupDict) != len(nums) 
#        duplicate =set()
#        for i in nums:
#            if i in duplicate:
#                return True
#            duplicate.add(i)
#        return False

