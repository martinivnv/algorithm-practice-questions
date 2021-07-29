# 07 23 2021
# Implement hash table from scratch.

class HashTable:
    def __init__(self, length=4):
        # Initiate our array with empty values.
        self.array = [None] * length

    def hash(self, key):
        # Get index of our array for a specific string key
        length = len(self.array)
        return hash(key) % length # Note that the hash used here is a built-in Python function

    def add(self, key, value):
        # Add a value to our array by its key
        index = self.hash(key)
        # If there is already some value at this index 
        if self.array[index] is not None:
            for kvp in self.array[index]:
                # If our key is found to already exist
                if kvp[0] == key:
                    # Update the value of the key
                    kvp[1] = value
                    break
            else:
                # If no existing key was found, add the kvp to the end
                self.array[index].append([key, value])
        # If this index is empty, initiate a new list and add our kvp to it
        else:
            self.array[index] = []
            self.array[index].append([key, value])
        # After adding, check if the array is now full and double it if need be
        if self.is_full():
            self.double()
    
    def get(self, key):
        # Get a value by key
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            # Loop through all key value pairs to find key
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]
            # If loop finishes and key is not found, it does not exist
            raise KeyError()

    def is_full(self):
        # Determines if the hash table is too populated
        items = 0
        # Count how many indexes in array are populated
        for item in self.array:
            if item is not None:
                items += 1
        # Return bool value based on if over half of indexes are populated
        return items > len(self.array) / 2

    def double(self):
        # Double length of list and copy over values
        ht2 = HashTable(length=len(self.array)*2)
        for i in range(len(self.array)):
            if self.array[i] is None: 
                continue
            # Since the array is a different length, different hash indexes will be generated
            # Values need to be re added
            else:
                for kvp in self.array[i]:
                    ht2.add(kvp[0], kvp[1])
        # Replace original array with the new array we just made
        self.array = ht2.array

    def __setitem__(self, key, value):
        self.add(key, value)
    
    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self.get(key) is not None:
            return True
        else:
            return False


if __name__ == '__main__':
    months = HashTable()
    months.add("01", "January")
    months.add("02", "February")
    months.add("03", "March")
    months.add("04", "April")
    months.add("05", "May")
    months.add("06", "June")
    months.add("07", "July")
    months.add("08", "August")
    months.add("09", "September")
    months.add("10", "October")
    months["11"] = "November"
    months["12"] = "Dec"
    months["12"] = "December"
    print(months["06"])
    print(months["11"])
    print(months.get("12"))
    if "01" in months:
        print("Found!")
    print(months.array)
