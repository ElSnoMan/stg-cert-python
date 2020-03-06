

""" As a user, I need to be able to count the number
of vowels in a given string. """


# Components
  # Footer
    # footer.js
    # footer.spec.js


# TEST REPO
# Framework
# Tests


# Test Case = input + output + oracle
def count_vowels(string):
    if not isinstance(string, str):
        return 'error'

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0
    for ch in string:
        if ch in vowels:
            count += 1
    return count


def test_vowels_foobar():
    word = 'foobar'
    assert count_vowels(word) == 3


def test_vowels_none():
    assert count_vowels(None) == 'error'
