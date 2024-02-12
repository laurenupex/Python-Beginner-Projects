my_list1 = [1, 2, 3, 4, 5, 6]
my_list2 = (1, 2, 3, 4, 5, 6)
# manually adds integers to list
# range command automatically adds integers in range

my_list3 = list(range(1, 7, 3))
# range goes from first number to second number-1
# third argument in range adds increments of that number

print(my_list1)
print(my_list3)
print(type(my_list1))
print(type(my_list2))
print(type(my_list3))
# declaring list with () instead of [] = tuple not list

# operations on lists
print(my_list1[2])
# prints 2nd element, but element count starts from 0
print(my_list1[-1])
# prints last element in list
print(my_list1[1:4])
# prints slice of list from 2nd-4th element (doesn't include element of second number)
print(len(my_list1))
# prints number of elements in list
print(max(my_list1), min(my_list1))
# prints largest and smallest element in list

my_list1.append(120)
print(my_list1)
# adds 120 to end of list

my_list1.reverse()
print(my_list1)
# reverses order of list

print(my_list1 + my_list3)
# prints first list followed by second list, in one list
