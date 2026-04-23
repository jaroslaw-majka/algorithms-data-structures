# https://leetcode.com/problems/valid-palindrome/description/

def is_palindrome(s: str) -> bool:
    text = "".join([symbol.lower() for symbol in s if symbol.isalpha() or symbol.isdigit()])

    left, right = 0, len(text) - 1

    while left < right:
        if not text[left] == text[right]:
            return False

        left += 1
        right -= 1

    return True


assert is_palindrome("A man, a plan, a canal: Panama") 
assert not is_palindrome("race a car")
assert is_palindrome("")
assert not is_palindrome("0P")
