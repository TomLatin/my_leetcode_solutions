from collections import defaultdict
from typing import List

# My solution
def count_pairs(n):
    # Calculate pairs using the formula n * (n - 1) // 2
    return n * (n - 1) // 2


def numIdenticalPairs(nums: List[int]) -> int:
    num_to_count_of_occurrence = defaultdict(int)
    for num in nums:
        num_to_count_of_occurrence[num] += 1
    num_of_pairs = 0
    for count_of_occurrence in num_to_count_of_occurrence.values():
        num_of_pairs += count_pairs(count_of_occurrence)
    return num_of_pairs
