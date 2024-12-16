from typing import List


def my_solution_plus_one(digits: List[int]) -> List[int]:
    s = ""
    for d in digits:
        s += str(d)
    s_plus_one = int(s) + 1
    res = []
    for d in str(s_plus_one):
        res.append(int(d))
    return res


# Time complexity: O(n)
# Space complexity: O(n)
def recursion_plus_one(digits: List[int]) -> List[int]:
    if not digits:
        return [1]

    if digits[-1] < 9:
        digits[-1] += 1
        return digits
    else:
        return recursion_plus_one(digits[:-1]) + [0]


# Time complexity: O(n)
# Space complexity: O(1)
def iteration_plus_one(digits: List[int]) -> List[int]:
    one = 1
    i = 0
    digits = digits[::-1]

    while one:
        if i < len(digits):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                one = 0
        else:
            digits.append(one)
            one = 0
        i += 1
    return digits[::-1]


# Time complexity: O(n)
# Space complexity: O(1)
def optimal_iteration_plus_one(digits: List[int]) -> List[int]:
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    return [1] + digits
