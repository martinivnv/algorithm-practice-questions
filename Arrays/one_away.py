# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to 
# check if they are one edit (or zero edits) away.
# 07 24 2021

# Hints:
# Start with the easy thing. Can you check each of the conditions separately?
# What is the relationship between the "insert character" option and the "remove character" option? Do these need to be two separate checks? 
# Can you do all three checks in a single pass? 
class Solver(object):
    def __init__(self):
        pass

    # O(N) time complexity and O(1) space complexity, where N is the length of the shorter string
    def check(self, string1, string2):
        if abs(len(string1) - len(string2)) > 1:
            return False
        elif string1 == string2:
            return False
        elif len(string1) > len(string2):
            return self.compare_strings(string1, string2)
        elif len(string2) > len(string1):
            return self.compare_strings(string2, string1)
        else:
            diff_found = False
            for i in range(len(string1)):
                if string1[i] != string2[i]:
                        if not diff_found:
                            diff_found = True
                        else:
                            return False
            return True
    
    def compare_strings(self, hi_string, lo_string):
        diff_found = False
        for i in range(len(lo_string)):
            if not diff_found:
                if hi_string[i] != lo_string[i]:
                    diff_found = True
            else:
                if hi_string[i+1] != lo_string[i]:
                    return False
        return True

if __name__ == "__main__":
    s = Solver()
    print(s.check("pale", "ple"))       # True
    print(s.check("pales", "pale"))     # True
    print(s.check("palest", "pale"))    # False
    print(s.check("pale", "pale"))      # False
    print(s.check("pale", "bale"))      # True
    print(s.check("pale", "bake"))      # False