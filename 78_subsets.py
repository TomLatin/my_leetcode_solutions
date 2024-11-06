import copy
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result = [[]]
    for num in nums:
        result += [curr + [num] for curr in result]
    return result


if __name__ == '__main__':
    print(subsets([1, 2, 3]))
