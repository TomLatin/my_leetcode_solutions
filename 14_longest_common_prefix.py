from typing import List


def my_solution_longest_common_prefix(strs: List[str]) -> str:
    if "" in strs:
        return ""
    start = 0
    end = len(strs[0])
    for word in strs[1:]:
        counter = 0
        if len(word) < end:
            end = len(word)
        for letter in word:
            if counter <= end - 1 and letter != strs[0][counter]:
                end = counter
                break
            counter += 1
    if start == end == 0:
        return ""
    return strs[0][start: end]
