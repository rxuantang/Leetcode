class Solution:
    def spiralOrder(self, matrix):
        result = []
        m = len(matrix)
        n = len(matrix[0])
        top, left, bottom, right = 0, 0, m-1, n-1

        while top <= bottom and left <= right:
            for j in range(left,right+1):
                result.append(matrix[top][j])
            top += 1

            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right -= 1

            if len(result) != n*m:
                for j in range(right,left-1,-1):
                    result.append(matrix[bottom][j])
                bottom -= 1

                for i in range(bottom,top-1,-1):
                    result.append(matrix[i][left])
                left += 1

        return result

if __name__ == "__main__":
    solution = Solution()

    assert solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    assert solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]

    print("passed all test cases!")
