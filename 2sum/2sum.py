# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        empty_dict = {} #creating an empty map to hold dict values
        
        #loop through all the integers in nums
        for i in range(len(nums)):

            #if the difference exists in the empty_dict map then return the key value pairs as indices
            if target - nums[i] in empty_dict:
                return [empty_dict[target - nums[i]],i]
            
            #if not present in the map, add the indices to the map
            else:
                empty_dict[nums[i]] = i

#alternate approach 
def twoSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left],array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []
