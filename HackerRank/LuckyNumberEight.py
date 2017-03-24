n = input().strip()

numbers_list = input().strip()

for i in range(len(numbers_list)):
    if numbers_list[i] != '0':
        break

numbers_list = numbers_list[i:len(numbers_list)]

for i in range(len(numbers_list) - 1, -1, -1):
    if numbers_list[i] not in ['1', '3', '5', '7', '9']:
        break

numbers, root_element, root_index = [], [], []
for v in numbers_list:

numbers = [int(n) for n in numbers_list]

root_set = set()
for i in range(len(numbers)):
    if numbers[i] not in root_set:
        root_set.add(numbers[i])
        prefix = numbers[i]
        for j in range(i + 1, len(numbers)):
            prefix = numbers[i:j]


