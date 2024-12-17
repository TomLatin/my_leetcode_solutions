from collections import Counter
from typing import List


def my_majority_element(nums: List[int]) -> int:
    c = Counter(nums)
    return c.most_common(1)[0][0]


def majorityElement(nums: List[int]) -> int:
    res, count = 0, 0
    for num in nums:
        if count == 0:
            res = num
        count += (1 if num == res else -1)
        return res
