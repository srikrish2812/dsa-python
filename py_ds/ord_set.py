from collections import OrderedDict

class OrderedSet():

    def __init__(self):
        self._data = OrderedDict()

    def add(self, item):
        self._data[item] = None

    def remove(self,item):
        del self._data[item]

    def discard(self, item):
        self._data.pop(item, None)

    def __contains__(self, item):
        return item in self._data

    def __repr__(self):
        return '{' + ', '.join(map(str, self._data)) + '}'

# Create an ordered set and insert elements
s = OrderedSet()
s.add(1)  # {1}
s.add(3)  # {1, 3}
s.add(5)  # {1, 3, 5}
s.add(7)  # {1, 3, 5, 7}
s.add(3)  # {1, 3, 5, 7} --> 3 doesn't get inserted

print(s)

# Erase elements from the ordered set
s.remove(3)  # Erase element '3'
s.discard(7)  # Erase element '7' using discard (won't raise an error if the element is not present)

print(s)

for i in [2, 4, 6, 8, 10]:
    s.add(i)

print(s)

count8 = 1 if 8 in s else 0
count5 = 1 if 5 in s else 0
print("Count of 8 in the set:", count8)  # 1
print("Count of 5 in the set:", count5)  # 0


from collections import Counter

# Create a Multi-Set using Counter
multi_set = Counter()

# Insert elements into the Multi-Set
multi_set.update([5])  # {5}
multi_set.update([2])  # {2, 5}
multi_set.update([5])  # {2, 5, 5}
multi_set.update([8])  # {2, 5, 5, 8}
multi_set.update([2])  # {2, 2, 5, 5, 8}
multi_set.update([5])  # {2, 2, 5, 5, 5, 8}
multi_set.update([9])  # {2, 2, 5, 5, 5, 8, 9}

# Erase elements from the Multi-Set
multi_set.subtract([5])  # {2, 2, 8, 9}

# Find
if 2 in multi_set:
    print("Found:", 2)  # Found

# Count
count = multi_set[2]
print("Count of 2:", count)  # 2


# Creating an unordered set
my_set = set()

# Insert operation
my_set.add(3)
my_set.add(4)
my_set.add(2)
my_set.add(0)
my_set.add(3) # Already exists, doesn't get added
my_set.add(2) # Already exists, doesn't get added
my_set.add(3) # Already exists, doesn't get added
# my_set = {0, 2, 3, 4} -> random order and just an example
print(my_set)
# Erase operation
my_set.remove(2)
print(my_set)
# Find operation
if 3 in my_set:
    print("Found 3")  # Found 3
else:
    print("Not found")

# Count operation
count = sum(1 for element in my_set if element == 0)
print("Count of 0:", count)  # 1
