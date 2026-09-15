class Solution:
    def isAnagram(self, s, t):
        from collections import defaultdict
        dict_s, dict_t = defaultdict(int), defaultdict(int)
        for i in s:
            dict_s[i] += 1
        
        for j in t:
            dict_t[j] += 1

        return dict_s == dict_t

if __name__ == "__main__":
    solution = Solution()

    assert solution.isAnagram("anagram", "nagaram") == True
    assert solution.isAnagram("rat", "car") == False

    print("passed all test cases!")

