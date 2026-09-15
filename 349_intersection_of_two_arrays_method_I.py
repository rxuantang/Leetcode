class Solution:
    def intersection(self, nums1, nums2):
        set_1 = set(nums1)
        set_2 = set(nums2)
        
        return list(set_1&set_2)

if __name__ == "__main__":
    solution = Solution()

    assert solution.intersection([1,2,2,1], [2,2]) == [2]
    assert solution.intersection([4,9,5], [9,4,9,8,4]) == [9,4]

    print("passed all test cases!")