from collections import defaultdict

# Creating a MultiMap-like structure
multi_map = defaultdict(list)

# Adding values
multi_map['apple'].append(1)
multi_map['apple'].append(2)
multi_map['banana'].append(3)

# Iterating over the MultiMap
for key, values in multi_map.items():
    print(key, values)

# Checking if a key exists
if 'apple' in multi_map:
    print("Apples:", multi_map['apple'])

# Adding more values
multi_map['apple'].extend([3, 4])
print(multi_map)
