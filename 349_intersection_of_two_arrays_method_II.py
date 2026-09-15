class Solution:
    def intersection(self, nums1, nums2):
        n = 1001
        record_1, record_2 = [0] * n, [0] * n
        for i in range(len(nums1)):
            record_1[nums1[i]] += 1
        
        for j in range(len(nums2)):
            record_2[nums2[j]] += 1

        result = []

        for k in range(n):
            if record_1[k] * record_2[k] > 0:
                result.append(k)
     
        return result

if __name__ == "__main__":
    solution = Solution()

    assert solution.intersection([1,2,2,1], [2,2]) == [2]
    assert solution.intersection([4,9,5], [9,4,9,8,4]) == [4,9]

    print("passed all test cases!")