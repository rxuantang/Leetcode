class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num

        while left <= right:
            mid = left + (right-left)//2
            if mid*mid > num:
                right = mid - 1
            elif mid*mid < num:
                left = mid + 1
            else: 
                return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()

    assert solution.isPerfectSquare(16) == True
    assert solution.isPerfectSquare(14) == False

    print("passed all test cases!")          
 