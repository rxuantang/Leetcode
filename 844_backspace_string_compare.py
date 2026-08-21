class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        lst_s = list(s)
        lst_t = list(t)
        fast_s, fast_t, slow_s, slow_t = 0, 0, 0, 0
        
        while fast_s < len(lst_s):
            if lst_s[fast_s] != "#":
                lst_s[slow_s] = lst_s[fast_s]
                slow_s += 1
            else:
                if slow_s > 0:
                    slow_s -= 1
                else:
                    slow_s = 0
            fast_s += 1

        while fast_t < len(lst_t):
            if lst_t[fast_t] != "#":
                lst_t[slow_t] = lst_t[fast_t]
                slow_t += 1
            else:
                if slow_t > 0:
                    slow_t -= 1
                else:
                    slow_t = 0
            fast_t += 1

        return lst_s[0:slow_s] == lst_t[0:slow_t]

if __name__ == "__main__":
    solution = Solution()

    assert solution.backspaceCompare("ab#c", "ad#c") == True
    assert solution.backspaceCompare("ab##", "c#d#") == True
    assert solution.backspaceCompare("a##c", "#a#c") == True
    assert solution.backspaceCompare("a#c", "b") == False

    print("passed all test cases!")

