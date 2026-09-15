class Solution:
    def isAnagram(self, s, t):
        record = [0] * 26
        for i in s:
            record[ord(i)-ord("a")] += 1
        
        for j in t:
            record[ord(j)-ord("a")] -= 1

        for k in record:
            if k != 0:
                return False
        
        return True

if __name__ == "__main__":
    solution = Solution()

    assert solution.isAnagram("anagram", "nagaram") == True
    assert solution.isAnagram("rat", "car") == False

    print("passed all test cases!")

