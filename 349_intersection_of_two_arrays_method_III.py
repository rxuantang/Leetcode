class Solution:
    def intersection(self, nums1, nums2):
        table = {}

        for num in nums1:
            table[num] = table.get(num,0) + 1
        
        result = set()
        for num in nums2:
            if num in table:
                result.add(num)
        
        return list(result)
        

if __name__ == "__main__":
    solution = Solution()

    assert solution.intersection([1,2,2,1], [2,2]) == [2]
    assert solution.intersection([4,9,5], [9,4,9,8,4]) == [9,4]

    print("passed all test cases!")