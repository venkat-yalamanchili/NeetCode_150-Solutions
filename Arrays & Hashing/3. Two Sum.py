class Solution:
    def twoSum(nums,target):
        lookup = {} # val -> index

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in lookup:
                return [lookup[diff], i]
            lookup[nums[i]] =  i