# Given a string, write a function to check if it is a permutation of a palindrome. 
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# 07 24 2021

# Hints:
# You do not have to-and should not-generate all permutations. This would be very inefficient. 
# What characteristics would a string that is a permutation of a palindrome have?
# Have you tried a hash table? You should be able to get this down to O(N) time. 
# Can you reduce the space usage by using a bit vector? 

class Solver(object):
    def __init__(self):
        pass

    # O(N) time complexity and 
    def check(self, str):
        if len(str) == 1:
            return True
        chars = {}
        # Store each letter/char in the string i a hash table
        # If the number of times that the char appears is even, store True
        # If the char appears an odd number of times, store False
        for letter in str:
            letter = letter.lower()
            if letter in chars:
                chars[letter] = not chars[letter]
            else:
                chars[letter] = False
        print(chars)
        
        # Check that all of the chars appear an even number of times
        # Up to one letter is allowed to appear an odd number of times ( if it is the middle )
        middle_found = False
        for letter, bool in chars.items():
            if bool is False:
                if not middle_found:
                    middle_found = True
                else:
                    return False
        return True

if __name__ == "__main__":
    s = Solver()
    print(s.check("racecar"))
    print(s.check("zzz"))
    print(s.check("cdcdcdaa"))
    print(s.check("saippuakivikauppias"))
    print(s.check("fjdkdalk"))