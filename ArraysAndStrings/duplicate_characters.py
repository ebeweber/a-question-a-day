"""Implement an algorithm to determine if a string has all
unique characters. Consider both a case where you can use addition
data structures and the case where you cannot."""


def unique_with_set(s):
    """Determines if a string has all unique characters using a set.
    Does so in O(n) extra space and O(n) time.

    :type s: String
    :param s: string to detect duplicate characters
    :rtype: bool
    :returns: boolean indicating whether or not duplicate characters
    """
    seen = set()
    for ch in s:
        if ch in seen:
            return False
        seen.add(ch)

    return True


def unique_constant_space(s):
    """Determines if a string has all unique characters using no
    additional space. Runs in O(nlogn) time with no additional space
    by sortng the string first.

    :type s: String
    :param s: string to detect duplicate characters
    :rtype: bool
    :returns: boolean indicating whether or not duplicate characters
    """
    s = "".join(sorted(s))

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False

    return True


def test(fnc):
    """Runs the test on function fnc"""
    assert(fnc("hello") == False)
    assert(fnc("asdfghjkl") == True)
    assert(fnc("asdfghh") == False)
    assert(fnc("") == True)


if __name__ == "__main__":
    test(unique_with_set)
    test(unique_constant_space)
