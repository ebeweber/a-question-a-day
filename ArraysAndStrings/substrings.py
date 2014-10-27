"""Find the longest common substring in two strings. If there are multiple
substrings of the same length this will return the first substring of length
l that it comes across, the others will be ignored.

Can easily be modified to return a set of substrings instead
"""

def longest_substring(s1, s2):
    """Takes two strings s1 and s2 and fills up a grid of substring matches.
    The grid contains pervious information, and is an example of how to solve
    this using dynamic programming.

    If finding the maximum common substring between the words 'working' and
    'workout' the grid would look like this:

       w  o  r  k  o  u  t
    w  0  0  0  0  0  0  0  0
    o  0  1  0  0  0  0  0  0
    r  0  0  2  0  0  1  0  0
    k  0  0  0  3  0  0  0  0
    i  0  0  0  0  4  0  0  0
    n  0  0  0  0  0  0  0  0
    g  0  0  0  0  0  0  0  0
       0  0  0  0  0  0  0  0
    """
    n = len(s1)
    m = len(s2)
    longest = 0
    longest_str = ""

    grid = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                # These letters match, shift the grid accordingly
                v = grid[i][j] + 1
                grid[i+1][j+1] = v

                # New longest, return this
                if v > longest:
                    longest = v
                    longest_str = s1[i-v+1:i+1]

    return longest_str


def test(fnc):
    assert(fnc("lollipop", "philologist") == "lol")
    assert(fnc("asnfhellosadklj", "iouewoihelloasnmb") == "hello")
    assert(fnc("", "") == "")


if __name__ == "__main__":
    test(longest_substring)
