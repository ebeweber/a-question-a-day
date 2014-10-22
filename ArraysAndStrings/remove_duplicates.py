"""Design an algorithm and write code to remove the duplicate characters in a
string without using any additional buffer. NOTE: One or two additional
variables are fine. An extra copy of the array is not.
"""

def remove_duplicates(s):
    """Removes all of the duplicate characters from a string without using
    any additional buffer or data structures.

    :type s: string
    :param s: string to remove duplicates from
    :rtype: string
    :returns: string with duplicates removed
    """
    s = list(s)

    i = 0
    while i < len(s):
        # Get that character and remove the rest of the characters
        # At this point you have never seen this character before.
        c = s[i]
        j = i + 1

        while j < len(s):
            if s[j] == c:
                del s[j]
            else:
                j += 1

        i += 1

    return "".join(s)


def remove_duplicates_with_set(s):
    """Removes all of the duplicate characters in O(n) time (assuming)
    deletion and shifting is constant time with the additional space used
    by a set.

    :type s: string
    :param s: string to remove duplicates from
    :rtype: string
    :returns: string with duplicates removed
    """
    s = list(s)
    seen = set()
    i = 0

    while i < len(s):
        if s[i] in seen:
            del s[i]
        else:
            seen.add(s[i])
            i += 1

    return "".join(s)


def test(fnc):
    """Tests the remove duplicates function on a few different inputs"""
    assert(fnc("aabbcc") == "abc")
    assert(fnc("asdfghjkl") == "asdfghjkl")
    assert(fnc("aaaaaaa") == "a")


if __name__ == "__main__":
    test(remove_duplicates)
    test(remove_duplicates_with_set)
