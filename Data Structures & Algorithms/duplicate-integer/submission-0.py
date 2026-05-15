class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupDict = {x: x for x in nums}
        return len(nums) != len(dupDict) 