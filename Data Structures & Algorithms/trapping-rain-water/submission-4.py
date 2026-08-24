class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        water = 0

        while left < right:
            if leftMax <= rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                water += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                water += rightMax - height[right]

        return water



'''        
        limit = len(height)
        i, j = 0, 0
        leftMax, rightMax = [], []
        water = 0
        
        max = height[0]
        for i in height:
            if max < i:
                max = i
            leftMax.append(max)

        max = height[limit -1]
        for i in reversed(height):
            if max < i:
                max = i
            rightMax.append(max)

        rightMax.reverse() # because it was built in reverse

        for i in range(limit):
            water += min(leftMax[i], rightMax[i]) - height[i]   
    
        return water
'''

