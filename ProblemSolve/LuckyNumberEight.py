n = input().strip()

numbers = input().strip()

for i in range(len(numbers)):
    if numbers[i] != '0':
        break

numbers = numbers[i:len(numbers)]

for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] not in ['1', '3', '5', '7', '9']:
        break

numbers = [int(numbers[i]) for i in range(0, i + 1)]

divisible_count = numbers.count(8)

for i in range(len(numbers)):
    if numbers[i] != 0:
        prefix = numbers[i] % 8
        for j in range(i + 1, len(numbers)):
            prefix = (prefix * 10 + numbers[j]) % 8
            already_visited = set()
            for k in range(j + 1, len(numbers)):
                if numbers[k] not in already_visited:
                    number = prefix * 10 + numbers[k]
                    if number % 8 == 0:
                        divisible_count += 1
                    already_visited.add(numbers[k])
                    if len(already_visited) == 5:
                        break
print(divisible_count)
