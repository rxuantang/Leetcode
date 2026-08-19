class Solution:
    def removeElement(self, nums, val):
        fast = 0
        slow = 0
        length = len(nums)

        while fast < length:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow

if __name__ == "__main__":
    solution = Solution()

    assert solution.removeElement([3,2,2,3], 3) == 2
    assert solution.removeElement([0,1,2,2,3,0,4,2], 2) == 5

    print("passed all test cases!")