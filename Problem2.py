# 15. 3Sum

# Time Complexity: O(N^2)
# Space Complexity: O(1)
# Did this code successfully run on Leetcode: time limit exceeded
# Any problem you faced while coding this: No

# Approach: iterate over using 3 for loops and keep adding the list in the hashset, return the set with the unique lists

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        if not nums or len(nums) == 0:
            return []
        
        for i in range(0, len(nums)):
            
            for j in range(i+1, len(nums)):
                
                for k in range(j+1, len(nums)):
                    
                    if i!=j and j!=k and i!=k:
                        if nums[i]+nums[j]+nums[k] == 0:
                            temp = []
                            temp.append(nums[i])
                            temp.append(nums[j])
                            temp.append(nums[k])
                            result.append(sorted(temp))

        return set(tuple(row) for row in result)

# Time Complexity: O(N^2)
# Space Complexity: O(n)
# Did this code successfully run on Leetcode: time limit exceeded
# Any problem you faced while coding this: No

# Approach: 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if not nums or len(nums) == 0:
            return []
        
        # use i as the slow pointer or fix the pointer and find the 2 sum for 
        # rest of the array/ list
        
        result = []
        mymap = {}
        
        for i in range(0, len(nums)-2):
            
            sum_to_search = 0-nums[i]
            mymap = {}
            for j in range(i+1, len(nums)):
                
                    if sum_to_search-nums[j] in mymap and mymap[sum_to_search-nums[j]]!=j:
                        
                        temp = []
                        temp.append(nums[i]) 
                        temp.append(sum_to_search-nums[j])
                        temp.append(nums[j])
                        result.append(sorted(temp))

                    mymap[nums[j]] = j
        
        return set(tuple(row) for row in result)