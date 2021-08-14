# 11. Container With Most Water

# Time Complexity: O(N)
# Space Complexity: O(1)
# Did this code successfully run on Leetcode: yes
# Any problem you faced while coding this: No

# Approach: using 2 pointers, low and high from the 2 ends and iterating towards the middle based on the height


class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0
        low = 0
        high = len(height)-1
        
        while(low<high):
            
            area = (high-low) * min(height[high], height[low])
            if area > max_area:
                max_area = area
            if height[low] < height[high]:
                low = low + 1

            else:
                high = high - 1
        