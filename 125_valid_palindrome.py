import re


def MySolutionIsPalindrome(s: str) -> bool:
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    left_index = 0
    right_index = len(cleaned_text) - 1

    while right_index > left_index or right_index == left_index:
        if cleaned_text[right_index] != cleaned_text[left_index]:
            return False
        left_index += 1
        right_index -= 1

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
