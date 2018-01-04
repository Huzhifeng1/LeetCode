class Solution(object):
    def twoSum(self, nums, target):
        dict={}
        for num in nums:
            dict[nums.index(num)] = [num,target-num]

        for k,v in dict.iteritems():
            index1 = nums.index(v[0])
            if nums[:index1].__contains__(v[1]) or nums[index1+1:].__contains__(v[1]):
                return [index1,nums.index(v[1],index1+1)]

# test #
solu = Solution()
print solu.twoSum([3,3],6)
