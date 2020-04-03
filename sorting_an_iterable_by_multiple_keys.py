# Script that shows how to sort an iterable, in this case the items of a dictionary, using more than one key.

# Two different dictionaries, one with integers as values, and another one with lists (with two elements each) per list:
mydict1 = {
    "Jana": 10,
    "John": 7,
    "Simba": 10,
    "Anakin": 3,
    "Zach": 9,
    "Murray": 3,
    "Harry": 7,
}

mydict2 = {
    "Jana": [10, 4],
    "John": [7, 1],
    "Simba": [10, 1],
    "Anakin": [3, 6],
    "Zach": [9, 0],
    "Murray": [3, 6],
    "Harry": [7, 1],
}

# 1) Sorting the keys of mydict1 (e.g. names) alphabetically:
sorted_list_1 = [i for i in sorted(mydict1.keys(), key=lambda x: x)]
print("1) ", sorted_list_1)

# 2) Reverse-sorting by values of mydict1 (e.g. ints):
sorted_list_2 = [
    i for i in sorted(mydict1.values(), key=lambda x: x, reverse=True)
]
print("2) ", sorted_list_2)

# Note: because ints are being sorted, the same can be achieved this way:
sorted_list_2_1 = [i for i in sorted(mydict1.values(), key=lambda x: -x)]
print("2.1) ", sorted_list_2_1)

# 3) Reverse-sorting by mydict1 values (using the ints as sorting key):
sorted_list_3 = [i for i in sorted(mydict1.items(), key=lambda x: -x[1])]
print("3) ", sorted_list_3)

# Note: mydict1 key's can be retrieved as well (without the dict values):
sorted_list_3_1 = [i[0] for i in sorted(mydict1.items(), key=lambda x: -x[1])]
print("3.1) ", sorted_list_3_1)

# 4) Reverse-sorting by values and then sorting by keys (for the same int, names will be sorted alphabetically):
sorted_list_4 = [
    i
    for i in sorted(
        sorted(mydict1.items(), key=lambda x: x[0]),
        key=lambda x: x[1],
        reverse=True,
    )
]
print("4) ", sorted_list_4)

# Note: as previously shown, the last example could be also executed this way:
sorted_list_4_1 = [
    i for i in sorted(mydict1.items(), key=lambda x: (-x[1], x[0]))
]
print("4.1) ", sorted_list_4_1)

# 5) Using mydict2, this sorting will use as first key the first element on the list (reversed), as second key the second element, and as third key the names (reversed):
sorted_list_5 = [
    i
    for i in sorted(
        sorted(mydict2.items(), key=lambda x: x[0], reverse=True),
        key=lambda x: (-x[1][0], x[1][1]),
    )
]
print("5) ", sorted_list_5)

# As seen in sorted_list_5, Murray and Anakin, and John and Harry, who have the same values in their lists, appear in reverse alphabetical order, while Simba precedes Jana, because Simba's second value is lower than Jana's.
