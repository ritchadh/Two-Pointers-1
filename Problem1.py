# Sort Colors

# Time Complexity: O(n^2)
# Space Complexity: O(1) 
# Did this code successfully run on Leetcode: all test cases passed
# Any problem you faced while coding this: No

# Approach 1: Take all the multipliers from the left side of the array except for the number at the index itself, (running muliplication)
# Also, take all the multipliers from the right side. Multiply the result of both the array and return the output.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        place = -1
        ptr1 = 0
        while(place<1 and ptr1!=len(nums)-1):
            
            ptr2 = ptr1+1
            place = place+1
          
            while(ptr2!=len(nums)):
                
                if nums[ptr1] == place:
                    ptr1+=1
                    
                elif nums[ptr1]!=place and nums[ptr2] == place:
                    temp = nums[ptr1]
                    nums[ptr1] = nums[ptr2]
                    nums[ptr2] = temp
                    ptr1+=1
                ptr2+=1