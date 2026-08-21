class Solution:
    def minSubArrayLen(self, target, nums):
        min_length = float("inf")
        length = len(nums)
        i = 0
        j = 0
        sub_sum = 0

        while j < length:
            sub_sum += nums[j]
            while sub_sum >= target:
                min_length = min(j-i+1,min_length)
                sub_sum -= nums[i]
                i += 1
            j += 1

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