class Solution:
    def mySqrt(self, x):
        left = 0
        right = x

        while left <= right:
            mid = left + (right-left)//2
            if mid*mid > x:
                right = mid - 1
            elif mid*mid < x:
                left = mid + 1
            else:
                return mid

        return left-1

if __name__ == "__main__":
    solution = Solution()

    assert solution.mySqrt(4) == 2
    assert solution.mySqrt(8) == 2

    print("passed all test cases!")      
 