class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        length = len(nums)

        while i < length:
            if nums[i] == val:
                for j in range(i+1, length):
                    nums[j-1] = nums[j]
                i -= 1
                length -= 1
            i += 1
        
        return length

if __name__ == "__main__":
    solution = Solution()

    assert solution.removeElement([3,2,2,3], 3) == 2
    assert solution.removeElement([0,1,2,2,3,0,4,2], 2) == 5

    print("passed all test cases!")