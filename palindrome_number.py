"""
Check the given number is palindrome number or not;
Find the largest 2 product of given palindrome number;
"""


def is_palindrome(number):
    """
    check the given number is palindrome number;
    """
    num, result = str(number), False
    if num == num[::-1]:
        result = True
    return result


if __name__ == "__main__":
    print is_palindrome(1234)
    print is_palindrome(12321)
    print is_palindrome(1234567654321)
