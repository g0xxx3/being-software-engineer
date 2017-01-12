from collections import OrderedDict, MutableSet


class OrderedSet(OrderedDict, MutableSet):
    def update(self, *args, **kwargs):
        if kwargs:
            raise TypeError("update() takes no keyword arguments")

        for s in args:
            for e in s:
                self.add(e)

    def add(self, elem):
        self[elem] = None

    def discard(self, elem):
        self.pop(elem, None)

    def __le__(self, other):
        return all(e in other for e in self)

    def __lt__(self, other):
        return self <= other and self != other

    def __ge__(self, other):
        return all(e in self for e in other)

    def __gt__(self, other):
        return self >= other and self != other

    def __repr__(self):
        return 'OrderedSet([%s])' % (', '.join(map(repr, self.keys())))

    def __str__(self):
        return '{%s}' % (', '.join(map(repr, self.keys())))

    difference = property(lambda self: self.__sub__)
    difference_update = property(lambda self: self.__isub__)
    intersection = property(lambda self: self.__and__)
    intersection_update = property(lambda self: self.__iand__)
    issubset = property(lambda self: self.__le__)
    issuperset = property(lambda self: self.__ge__)
    symmetric_difference = property(lambda self: self.__xor__)
    symmetric_difference_update = property(lambda self: self.__ixor__)
    union = property(lambda self: self.__or__)

n = input().strip()

numbers_list = input().strip()

for i in range(len(numbers_list)):
    if numbers_list[i] != '0':
        break

numbers_list = numbers_list[i:len(numbers_list)]

for i in range(len(numbers_list) - 1, -1, -1):
    if numbers_list[i] not in ['1', '3', '5', '7', '9']:
        break

numbers = []
root_set = OrderedSet()

for i in range(0, i + 1):
    v = int(numbers_list[i])
    root_set.add(v)
    numbers.append(v)

divisible_count = 0
if 8 in root_set:
    divisible_count = 1

root_set = list(root_set)

for r in root_set:
    if root_set != 0:
        for i in range(0, len(root_set)):
            if i == 0:
                prefix = r
            else:
                prefix = r * 10 + root_set[i]

            already_visited = set()
            for j in range(i + 1, len(numbers)):
                if len(already_visited) == 10:
                    break

                if numbers[j] not in already_visited:
                    number = prefix * 10 + numbers[j]
                    if number % 8 == 0:
                        divisible_count += 1
                    already_visited.add(numbers[j])

print(divisible_count)
