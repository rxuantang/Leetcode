class Solution:
    def isAnagram(self, s, t):
        from collections import Counter

        return Counter(s) == Counter(t)

if __name__ == "__main__":
    solution = Solution()

    assert solution.isAnagram("anagram", "nagaram") == True
    assert solution.isAnagram("rat", "car") == False

    print("passed all test cases!")

