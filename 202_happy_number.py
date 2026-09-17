class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()

        while n not in record:
            record.add(n)
            new_number = 0
            n_string = str(n)
            for i in n_string:
                new_number += int(i)**2
            if new_number == 1:
                return True
            else:
                n = new_number
        
        return False

if __name__ == "__main__":
    solution = Solution()

    assert solution.isHappy(19) == True
    assert solution.isHappy(2) == False

    print("passed all test cases!")