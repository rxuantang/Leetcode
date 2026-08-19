class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
                temp_val = nums[i]
                if (target - temp_val) in nums[i+1:len(nums)]:
                    return [i,nums[i+1:len(nums)].index(target - temp_val)+i+1]
                else:
                    continue

if __name__ == "__main__":
    solution = Solution()

    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]

    print("passed all test cases!")