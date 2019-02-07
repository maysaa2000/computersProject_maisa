x = [-1, -2, -3, -4, 6, 7, 7.1]
y = [7.2, 8.3, 9.1, 9.9, 0.2, -1, -1.05]
dx = [0.01, 0.01, 0.02, 0.04, 0.01, 0.02,0.02]
dy = [0.2, 0.1, 0.3, 0.1, 0.11, 0.02, 0.2]


def calculations (x,y,dx,dy):
    n = len(x)
    x_ave = sum(x) / n
    x_ave_2 = x_ave ** 2
    x_2 = [x * x for x, x in zip(x, x)]
    x_2_ave = sum(x_2) / n

    y_ave = sum(y) / n

    xy = [x * y for x, y in zip(x, y)]
    xy_ave = sum(xy) / n

    dy_2 = [dy * dy for dy, dy in zip(dy, dy)]
    dy_2_ave = sum(dy_2) / n

    a = ((xy_ave - x_ave * y_ave) / (x_2_ave - x_ave_2))
    b = y_ave - a * x_ave
    da = (dy_2_ave / (n * (x_2_ave - x_ave_2))) ** 0.5
    db = ((dy_2_ave * x_2_ave) / (n * (x_2_ave - x_ave_2))) ** 0.5
    chi2 = 0
    # calculating chi square
    for i in range(n):
        c = ((y[i] - (a * x[i] + b)) / dy[i]) ** 2
        chi2 += c
    chi2_reduced = chi2 / (n - 2)

    print("a = {} +- {}".format(a, da))
    print("b = {} +- {}".format(b, db))
    print("chi2 = {} ".format(chi2))
    print("chi2_reduced = {} ".format(chi2_reduced))

calculations (x,y,dx,dy)

