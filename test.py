eg_list = [10,20,30,40,50]

print(eg_list[::2]) # [10,30,50]

print(eg_list.pop(2)) # removes and returns the element at index 2 in rg_list
eg_list.insert(2,25) # inserts 25 at index 2
print(eg_list) # [10,20,25,40,50]

print(eg_list[4:0:-1]) # [50, 40, 25, 20]
print(eg_list[::-2]) # [50, 25, 10]
