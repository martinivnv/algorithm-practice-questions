# Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string.
# 07 23 2021

# Hints:
# It's often easiest to modify strings by going from the end of the string to the beginning. 
# You might find you need to know the number of spaces. Can you just count them?

class Solver(object):
    def __init__(self):
        pass

    # O(N^2) time and O(1) space, N being the true length of the string
    def urlify(self, str, true_length):
        num_spaces = 0
        # Count number of spaces in the "true length" part of the string
        for i in range(true_length):
            if str[i] == " ":
                num_spaces += 1

        # Find index of last character in the final string
        index = true_length + num_spaces * 2
        str_list = list(str)
        # Loop through the "true string" backwards
        for j in range(true_length-1, -1, -1):
            # When a space is found, replace it
            if str_list[j] == " ":
                str_list[index-1] = "0"
                str_list[index-2] = "2"
                str_list[index-3] = "%"
                index = index - 3
            # If the character is not a space, move it to the end of the string list
            else:
                str_list[index - 1] = str_list[j]
                index -= 1
        
        return "".join(str_list)

if __name__ == "__main__":
    s = Solver()
    print(s.urlify("Mr John Smith    ", 13))