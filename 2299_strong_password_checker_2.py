import re


def strongPasswordCheckerII(s: str) -> bool:
    if len(s) < 8:
        return False

    if (re.search(r'[a-z]', s) and
            re.search(r'[A-Z]', s) and
            re.search(r'\d', s) and
            # r"[^\w]" matches any character that is not a word character (excluding letters, digits, and underscore)
            # If I want to use r'["!@#$%^&*()+\-"]' I need to escape the special characters!!
            re.search(r'[^\w]', s) and
            # r"(.)\1+" means contain 2 of the same character in adjacent positions
            not re.search(r"(.)\1+", s)):
        return True
    return False
