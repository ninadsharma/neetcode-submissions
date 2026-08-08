class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort() #SpaceSaving Sort

        results = []

        i , j, k = 0, 1, len(nums) - 1

        while i < len(nums) - 2 :
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                current = nums[i] + nums[j] + nums[k]

                if current < 0:
                    j += 1
                elif current > 0:
                    k -= 1
                else:
                    results.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]: j += 1
                    while j < k and nums[k] == nums[k+1]: k -= 1
            i += 1

        return results