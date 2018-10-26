# my_tup = ('diamond', 'club', 'spade', 'heart')
# # print(my_tup[::2])
# # print(my_tup[0:1])
# # print(my_tup[0])
# # print(my_tup[0::2])
#
# for i in my_tup:
#     print(my_tup[i]\n)

# tuple is storing playing card suits
#because the tuple uses indexes to store data


# my_dct = {'Texas': 'Austin', 'Indiana': 'Indianapolis', 'Illinois': 'Chicago', 'New York': 'New York City'}
# for element in my_dct:
#     print(element)
#
#
# my_set = {2, 3, 5}
# for num in my_set:
#     print(num)


# values = raw_input("Please enter comma sep: ")
# l = values.split(",")
# print(l)
# alternate = tuple(l[0:2]), tuple(l[2:4]), tuple(l[4:6])
# print(alternate)
# my_list = [alternate]
# print(my_list)
# # my_tup = tuple(alternate)
# # print(my_tup
#     # print(l)
#     # print(t)
#     # print('List : ', l)
#     # print('Tuple : ',t)


values = raw_input("Please enter numbers sep by dashes: ")
input_split = values.split("-")
numbers = [int(x) for x in input_split]
print(numbers)
my_dict = {}
for num in numbers:
    keys = num
    print(keys)
    values = (num**2)
    my_dict[keys] = values
print(my_dict)
