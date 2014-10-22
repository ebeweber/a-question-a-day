"""Write a method to decide if two strings are anagrams or not. Two strings
are anagrams if the contain all the same letters just scrambled in some other
order."""

def anagrams_naive(s1, s2):
    """Detects whether two strings are anagrams.

    :type s1: string
    :param s1: the first string
    :type s2: string
    :param s2: the first string
    :rtype: bool
    :returns: whether or not the two strings are anagrams
    """
    return "".join(sorted(s1)) == "".join(sorted(s2))


def anagrams(s1, s2):
    """Detects whether two strings are anagrams in O(n) time using a set

    :type s1: string
    :param s1: the first string
    :type s2: string
    :param s2: the first string
    :rtype: bool
    :returns: whether or not the two strings are anagrams
    """
    # chr -> count mapping
    letter_counts = dict()

    # Count up the letters seen in the first string
    for ch in s1:
        letter_counts[ch] = (
            letter_counts[ch] + 1 if ch in letter_counts.keys() else 1
        )

    # Verify letter counts match in the second string
    for ch in s2:
        if ch in letter_counts.keys():
            letter_counts[ch] = letter_counts[ch] - 1
        else:
            return False

    # Verify all the letter counts are back to zero
    for ch in letter_counts.keys():
        if letter_counts[ch] != 0:
            return False

    return True





def test(fnc):
    """Tests the function to see if it detects anagrams appropriately"""
    assert(fnc("abc", "cba") == True)
    assert(fnc("", "") == True)
    assert(fnc("asdfghjkl", "lkjhgfdsa") == True)
    assert(fnc("asjdla", "wieuqe") == False)

if __name__ == "__main__":
    test(anagrams_naive)
    test(anagrams)
