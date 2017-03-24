# https://www.hackerrank.com/challenges/python-tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = [int(x) for x in input().split()]
    print(hash(tuple(integer_list)))
