class Solution:
    def removeElement(self, nums, val):
        fast = 1
        slow = 1
        length = len(nums)

        while fast < length:
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow

if __name__ == "__main__":
    solution = Solution()

    assert solution.removeElement([1,1,2], 1) == 2
    assert solution.removeElement([0,0,1,1,2,2,3,3,4], 2) == 5

    print("passed all test cases!")