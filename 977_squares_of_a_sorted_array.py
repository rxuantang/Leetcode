class Solution:
    def sortedSquares(self, nums):
        left = 0
        right = len(nums) - 1
        i = len(nums) - 1
        res = [0] * len(nums)

        while left <= right:
            if nums[left]*nums[left] < nums[right]*nums[right]:
                res[i] = nums[right]*nums[right]
                right -= 1
                i -= 1
            else:
                res[i] = nums[left]*nums[left]
                left += 1
                i -= 1
        
        return res

if __name__ == "__main__":
    solution = Solution()

    assert solution.sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
    assert solution.sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]

    print("passed all test cases!")