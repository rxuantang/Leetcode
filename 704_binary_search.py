class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return -1

if __name__ == "__main__":
    solution = Solution()

    assert solution.search([-1,0,3,5,9,12], 9) == 4
    assert solution.search([-1,0,3,5,9,12], 2) == -1

    print("passed all test cases!")