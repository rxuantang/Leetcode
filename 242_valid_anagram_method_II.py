class Solution:
    def isAnagram(self, s, t):
        record_s, record_t = [0] * 26, [0] * 26
        for i in s:
            record_s[ord(i)-ord("a")] += 1
        
        for j in t:
            record_t[ord(j)-ord("a")] += 1

        return record_s == record_t

if __name__ == "__main__":
    solution = Solution()

    assert solution.isAnagram("anagram", "nagaram") == True
    assert solution.isAnagram("rat", "car") == False

    print("passed all test cases!")

