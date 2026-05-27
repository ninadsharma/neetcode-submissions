class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            for j in range(1,len(nums)):
                if nums.index(i) != j:
                    if i + nums[j] == target:
                        return [nums.index(i),j]
        return [0,0]
        