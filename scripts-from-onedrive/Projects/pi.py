def calc_pi():
    pi = 0
    n = 4
    d = 1
    for i in range(1, 10000000):
        a = 2*(i%2)-1
        pi += a*n/d
        d += 2
    return pi

print(calc_pi())
