import re


def MySolutionIsPalindrome(s: str) -> bool:
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    right_index = 0
    left_index = len(cleaned_text) - 1

    while left_index > right_index or left_index == right_index:
        if cleaned_text[left_index] != cleaned_text[right_index]:
            return False
        right_index += 1
        left_index -= 1

    return True


def isPalindrome(s: str) -> bool:
    newStr = ''
    for c in s:
        if c.isalnum():
            newStr += c.lower()
    return newStr == newStr[::-1]


if __name__ == '__main__':
    s = "0P"
    isPalindrome(s)
