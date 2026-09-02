class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:(m+n)] = nums2
        for i in range(len(nums1)):
            min_idx = i
            for j in range(i+1,len(nums1)):
                if nums1[j] < nums1[min_idx]:
                    min_idx = j
            nums1[i], nums1[min_idx] = nums1[min_idx], nums1[i]
            
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