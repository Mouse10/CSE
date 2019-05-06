test_num = "6943058734720510"

numbers_lists = list(test_num)
print(numbers_lists)


def validate(num: str):
    numbers_lists.pop(15)
    print(numbers_lists)
    reversed_list = numbers_lists[::-1]
    print(reversed_list)
    for index in range(len(reversed_list)):
        reversed_list[index] = int(reversed_list[index])
        if index
    print(reversed_list)
print(validate(test_num))