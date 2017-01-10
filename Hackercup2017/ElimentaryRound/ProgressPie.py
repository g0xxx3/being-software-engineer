# https://www.facebook.com/hackercup/problem/1254819954559001/

from math import atan, degrees


def check_region(_p, _x, _y):
    if _p == 0:
        return 'white'

    angle, delta_x, delta_y, r_2 = (_p * 360.0) / 100.0, 50 - _x, 50 - _y, 50 * 50
    delta_r_2 = delta_x * delta_x + delta_y * delta_y

    if delta_y == 0:
        if _x > 50:
            delta_angle = 0.0
        else:
            delta_angle = 180.0
    else:
        delta_angle = degrees(atan(delta_x / delta_y))
    if angle >= delta_angle and r_2 >= delta_r_2:
        return 'black'
    return 'white'

input_file = open('progress_pie.txt', 'r')
output_file = open('progress_pie_output.txt', 'w')
n = int(input_file.readline())
for i in range(1, n + 1):
    p, x, y = map(int, input_file.readline().split())
    print('Case #{0}: {1}'.format(i, check_region(p, x, y)), file=output_file)
input_file.close()
