from typing import List


def remove_duplicates_not_inplace(nums: List[int]) -> int:
    before = nums[0]
    k = 1
    res = [nums[0]]
    for curr in nums[1:]:
        if before != curr:
            k += 1
            res.append(curr)
        before = curr

    if len(res) < len(nums):
        for i in range(len(nums) - len(res)):
            res.append("_")

    return k

# O(n^2) time complexity because of the index() method
def remove_duplicates_my_solution(nums: List[int]) -> int:
    l, r = 0, 1
    k = 1
    there_is_underscore = False
    while r < len(nums):
        if nums[l] == nums[r]:
            nums[r] = "_"
            if not there_is_underscore:
                there_is_underscore = True
            r += 1
        else:  # nums[l] != nums[r]
            k += 1
            if there_is_underscore:
                first_underscore_index = nums.index("_", 0, r)
                nums[first_underscore_index] = nums[r]
                nums[r] = "_"
            r += 1
            l += 1
    return k

# O(n)
def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    l_unique_elements = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l_unique_elements] = nums[r]
            l_unique_elements += 1
    return l_unique_elements

if __name__ == '__main__':
    print(removeDuplicates([1, 1, 2]))
    print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(removeDuplicates([1, 1, 1, 1, 1, 1, 1]))
