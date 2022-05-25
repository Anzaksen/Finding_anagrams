# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    sorted1 = sorted(word1)
    sorted2 = sorted(word2)
    if sorted1 == sorted2:
        return True
    else:
        return False


