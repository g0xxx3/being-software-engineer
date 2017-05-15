# Number Max: Write a method that finds the maximum of two numbers. You should not use if-else
# or any other comparison operator.

def flip(bit):
    return 1 ^ bit

def get_sign(a):
    return (a >> 31) & 0x1


if __name__ == '__main__':
    # Generate input data
    a, b = map(int, input().strip().split())
    k = get_sign(a-b)
    q = flip(k)
    print(a * q + b * k)