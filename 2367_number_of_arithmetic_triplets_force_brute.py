class Solution:
    def arithmeticTriplets(self, nums, diff):
        count = 0

        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                if nums[j] - nums[i] == diff:
                    for k in range(j+1,len(nums)):
                        if nums[k] - nums[j] == diff:
                            count += 1
                        else:
                            continue
                else:
                    continue
                
        return count

if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums = [0, 1, 4, 6, 7, 10]
    diff = 3
    assert solution.arithmeticTriplets(nums, diff) == 2

    # Test case 2
    nums = [4, 5, 6, 7, 8, 9]
    diff = 2
    assert solution.arithmeticTriplets(nums, diff) == 2

    # Test case 3
    nums = [1, 2, 3, 4]
    diff = 1
    assert solution.arithmeticTriplets(nums, diff) == 2

    print("passed all test cases!")