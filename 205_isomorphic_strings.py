from collections import defaultdict

# O(n)
def my_solution_is_isomorphic(s: str, t: str) -> bool:
    letter_to_indexes_in_s = defaultdict(list)
    letter_to_indexes_in_t = defaultdict(list)
    if len(s) != len(t):
        return False
    for i, (l_in_s, l_in_t) in enumerate(zip(s, t)):
        letter_to_indexes_in_s[l_in_s].append(i)
        letter_to_indexes_in_t[l_in_t].append(i)
    for l_in_s, l_in_t in zip(letter_to_indexes_in_s.values(), letter_to_indexes_in_t.values()):
        if l_in_s != l_in_t:
            return False
    return True

# O(n)
def isIsomorphic(self, s: str, t: str) -> bool:
    mapST, mapTS = {}, {}

    for i in range(len(s)):
        c1, c2 = s[i], t[i]
        if ((c1 in mapST and mapST[c1] != c2) or
                (c2 in mapTS and mapTS[c2] != c1)):
            return False
        mapST[c1] = c2
        mapTS[c2] = c1

    return True


if __name__ == '__main__':
    print(isIsomorphic(s="egg", t="add"))
