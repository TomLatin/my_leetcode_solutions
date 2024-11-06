from collections import Counter
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    return [k for k, v in Counter(nums).most_common(k)]


# If we are not allowed to use Counter:
def topKFrequentWithoutCounter(nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)

    for key, key_freq in count.items():
        freq[key_freq].append(key)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


# The trick here is to use the index as the number of times we saw the value (reverse bucket sort)

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(topKFrequentWithoutCounter(nums, k))