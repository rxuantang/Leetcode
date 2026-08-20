class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        fast = 0
        slow = 0
        length = len(nums)

        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
                length -= 1
            fast += 1
        
        nums[slow:fast] = [0] * length

        ### no return in leetcode, but for testing purpose, I return the nums
        return nums


if __name__ == "__main__":
    solution = Solution()

    assert solution.moveZeroes([0,1,0,3,12]) == [1,3,12,0,0]
    assert solution.moveZeroes([0]) == [0]

    print("passed all test cases!")          
 