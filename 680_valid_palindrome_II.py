import re


def validPalindrome(s: str) -> bool:
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    left_index = 0
    right_index = len(cleaned_text) - 1

    while left_index < right_index:
        if cleaned_text[right_index] != cleaned_text[left_index]:
            skip_left = s[left_index + 1: right_index + 1]
            skip_right = s[left_index: right_index]
            return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
        left_index += 1
        right_index -= 1
    return True
