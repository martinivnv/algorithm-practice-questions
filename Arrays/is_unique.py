# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
# Assuming ASCII with 128 characters
# 07 23 2021

class String(object):
    def __init__(self, string):
        self.string = string

    # Solution takes roughly O(N) space and O(N^2) time
    """
    def is_unique(self):
        if len(self.string) > 128:
            return False
        chars = []
        for char in self.string:
            if char in chars:
                return False
            else:
                chars.append(char)
        return True
    """

    # Solution takes O(1) space and O(N) time
    def is_unique(self):
        if len(self.string) > 128:
            return False
        char_set = [None] * 128
        for char in self.string:
            char_index = ord(char)
            # If character has already been found
            if char_set[char_index]:
                return False
            else:
                char_set[char_index] = True
        return True

if __name__ == "__main__":
    s = String("bajyqwieorblokpms")
    t = String("QWERTYUIOPasdfghjkl123456789")
    u = String("")
    v = String("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890/#$*((")
    print(s.is_unique())
    print(t.is_unique())
    print(u.is_unique())
    print(v.is_unique())