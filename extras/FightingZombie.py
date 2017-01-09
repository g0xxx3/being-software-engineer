#!/bin/python3


def calculate_value(spell):
    i = spell.find('d')
    j = i + 1
    while j < len(spell):
        if spell[j] == '+' or spell[j] == '-':
            break
        j += 1
    return int(spell[0:i]), int(spell[i + 1:j]), 0 if spell[j:len(spell)] == '' else int(spell[j:len(spell)])


def calculate_probability(_x, _y, _c, _h, _v):
    _h -= _x * _v + _c
    if _h <= 0:
        return 1/_y
    if x == 0:
        return 0


input_file = open('fighting_the_zombie_example_input.txt', 'r')
output_file = open('fighting_the_zombie_example_output.txt', 'w')

t = int(input_file.readline())
for case_no in range(1, t + 1):
    h, s = map(int, input_file.readline().split())
    spells = [calculate_value(spell) for spell in input_file.readline().split()]
    for x, y, c in spells:
        for i in range(1, i + 1):
            calculate_probability(x, y, c, h, i)

    print('Case #{0}: {1}'.format(case_no, spells))

input_file.close()
