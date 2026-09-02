class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:(m+n)] = nums2
        gap = len(nums1) // 2
        while gap > 0:
            for i in range(gap,len(nums1)):
                key = nums1[i]
                j = i 
                while j >= gap and nums1[j-gap] > key:
                    nums1[j] = nums1[j-gap]
                    j -= gap
                nums1[j] = key
            gap //= 2
            
        return nums1 # just for testing purposes

if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    assert solution.merge(nums1, m, nums2, n) == [1, 2, 2, 3, 5, 6]

    # Test case 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    assert solution.merge(nums1, m, nums2, n) == [1]

    # Test case 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    assert solution.merge(nums1, m, nums2, n) == [1]

    print("passed all test cases!")