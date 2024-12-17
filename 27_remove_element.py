from typing import List


def removeElement(nums: List[int], val: int) -> int:
    if not nums:
        return 0
    k = 0
    for r, num in enumerate(nums):
        if num != val:
            nums[k] = num
            k += 1
    return k

if __name__ == '__main__':
    print(removeElement([2], 3))
    print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
