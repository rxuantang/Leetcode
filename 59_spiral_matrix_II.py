class Solution:
    def generateMatrix(self, n):
        result = [[0]*n for _ in range(n)]
        startx, starty = 0, 0
        loop, mid = n//2, n//2 
        count = 1

        for offset in range(1,loop+1):
            for j in range(starty, n-offset):
                result[startx][j] = count
                count += 1
            for i in range(startx, n-offset):
                result[i][n-offset] = count
                count += 1
            for j in range(n-offset,starty,-1):
                result[n-offset][j] = count
                count += 1
            for i in range(n-offset,startx,-1):
                result[i][starty] = count
                count += 1
            startx += 1
            starty += 1

        if n%2 != 0:
            result[mid][mid] = count

        return result

if __name__ == "__main__":
    solution = Solution()

    assert solution.generateMatrix(3) == [[1,2,3],[8,9,4],[7,6,5]]
    assert solution.generateMatrix(4) == [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]

    print("passed all test cases!")