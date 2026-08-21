class Solution:
    def minSubArrayLen(self, target, nums):
        min_length = float("inf")
        length = len(nums)
        for i in range(length):
            sub_sum = 0
            for j in range(i,length):
                sub_sum += nums[j]
                if sub_sum >= target:
                    min_length=min(min_length,j-i+1)
        
        if min_length == float("inf"):
            return 0
        else:
            return min_length

if __name__ == "__main__":
    solution = Solution()

    assert solution.minSubArrayLen(7, [2,3,1,2,4,3]) == 2
    assert solution.minSubArrayLen(4, [1,4,4]) == 1
    assert solution.minSubArrayLen(11, [1,1,1,1,1,1,1,1]) == 0

    print("passed all test cases!")