# https://www.facebook.com/hackercup/problem/169401886867367/


#!/bin/python3

input_file = open('lazy_loading.txt', 'r')
output_file = open('lazy_loading_output.txt', 'w')

t = int(input_file.readline())
for i in range(1, t + 1):
    n = int(input_file.readline())
    weights = sorted([50 // (int(input_file.readline()) + 1) for _ in range(n)])

    top_item, next_item = 0, len(weights) - 1
    while top_item <= next_item:
        advance = weights[top_item]
        next_item -= advance
        if top_item <= next_item:
            top_item += 1
    print('Case #{0}: {1}'.format(i, top_item), file=output_file)
input_file.close()
