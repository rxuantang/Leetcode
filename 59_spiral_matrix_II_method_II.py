class Solution:
    def generateMatrix(self, n):
        result = [[0]*n for _ in range(n)]
        top, left, bottom, right = 0, 0, n-1, n-1
        count = 1

        while top <= bottom and left <= right:
            for j in range(left,right+1):
                result[top][j] = count
                count += 1
            top += 1

            for i in range(top,bottom+1):
                result[i][right] = count
                count += 1
            right -= 1

            for j in range(right,left-1,-1):
                result[bottom][j] = count
                count += 1
            bottom -= 1

            for i in range(bottom,top-1,-1):
                result[i][left] = count
                count += 1
            left += 1

        return result

if __name__ == "__main__":
    solution = Solution()

    assert solution.generateMatrix(3) == [[1,2,3],[8,9,4],[7,6,5]]
    assert solution.generateMatrix(4) == [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]

    print("passed all test cases!")