# Given two strings, write a method to decide if one is a permutation of the other
# 07 23 2021

# Brute force solution pesudocode with O(N^2) time:
"""
Loop through first string and check if each character is in the second string
"""

class Solver(object):
    def __init__(self):
        pass

    # Solution with O(N log N) time using built in sorted() function
    def check(self, string1, string2):
        if len(string1) != len(string2):
            return False
        return sorted(string1) == sorted(string2)

if __name__ == "__main__":
    s = Solver()
    print(s.check("cat", "tac"))
    print(s.check("hehw23", "hehw2"))
    print(s.check("doge", "dogy"))
    print(s.check("count_olaf", "al_funcoot"))