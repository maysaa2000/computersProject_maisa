#handling row inputs
def input_row (data):
    #improve every line in the data(except the last two) by:
    #turnig all letter to small letters
    #turnig the string to a list
    for line in data[0:len(data) - 2]:
        line_improved = line.strip('\n').lower().split()
        axis = line_improved[0]
        # finding the x axis and turnig it's elements to float
        if axis == 'x':
            x = list(map(float, line_improved[1:]))
        # finding the y axis and turnig it's elements to float
        elif axis == 'y':
            y = list(map(float, line_improved[1:]))
        # finding the x uncertainties and turnig it's elements to float
        elif axis == 'dx':
            dx = list(map(float, line_improved[1:]))
        # finding the y uncertainties and turnig it's elements to float
        elif axis == 'dy':
            dy = list(map(float, line_improved[1:]))

    if len(x) != len(y) or len(x) != len(dy) or len(x) != len(dx):
        print(" Data lists are not the same length.")
        exit()
    for test in dx:
        if test <= 0:
            print('Input file error: Not all uncertainties are positive.')
            exit()
    for test in dy:
        if test <= 0:
            print('Not all uncertainties are positive.')
            exit()
    return(x, y, dx, dy)


#handling colums inputs
def input_colums(data):
    data_improved_1 = []
    # improve every line in the data and adding  in to data_improved_1 (except the last two) by:
    # turnig all letter to small letters
    # turnig the string to a list
    for line in data[:len(data) - 2]:
        line_improved = line.strip('\n').lower().split()
        data_improved_1.append(line_improved)
    row = len(data_improved_1)
    colums = len(data_improved_1[0])
    data_improved = []
    #tring to turn the colums of data_improved_1 to rows
    try:
        for c in range(colums):
            helper = []
            for r in range(row):
                helper.append(data_improved_1[r][c])
            # print(helper)
            data_improved.append(helper)
    #if the try statment didn't work then the length of the colums is diffrent
    except:
        print(" Data lists are not the same length.")
        exit()
    # print(data_improved)
    for l in data_improved:
        axis = l[0]
        # finding the x axis and turnig it's elements to float
        if axis == 'x':
            x = list(map(float, l[1:]))
        # finding the y axis and turnig it's elements to float
        elif axis == 'y':
            y = list(map(float, l[1:]))
        # finding the x uncertainties and turnig it's elements to float
        elif axis == 'dx':
            dx = list(map(float, l[1:]))
        # finding the y uncertainties and turnig it's elements to float
        elif axis == 'dy':
            dy = list(map(float, l[1:]))
    for test in dx:
        if test <= 0:
            print('Not all uncertainties are positive.')
            exit()
    for test in dy:
        if test <= 0:
            print('Not all uncertainties are positive.')
            exit()
    return (x, y, dx, dy)


#handling the file
def input_handling(file_name):
    file = open(file_name)
    data = file.readlines()
    axis_list = ['x', 'y', 'dx', 'dy']
    count = 0
    y_axis_title = data[len(data) - 1].strip('y axis :')
    x_axis_title = data[len(data) - 2].strip('x axis :')
    #determinig if the inputs are colums or rows
    for axis in axis_list:
        if axis in data[0].lower():
            count += 1
    t = input_colums(data) if count == 4 else input_row(data)
    x, y, dx, dy= t
    return(x, y, dx, dy,x_axis_title,y_axis_title)

#receive x y and their uncertainties
#calculate and print the outputs
def calculations (x,y,dx,dy):
    n=len(x)
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
    #calculating chi square
    for i in range(n):
        c = ((y[i] - (a * x[i] + b)) / dy[i]) ** 2
        chi2 += c
    chi2_reduced = chi2 / (n - 2)

    print("a = {} +- {}".format(a, da))
    print("b = {} +- {}".format(b, db))
    print("chi2 = {} ".format(chi2))
    print("chi2_reduced = {} ".format(chi2_reduced))

    return(a,b)

#receive x y and their uncertainties and titles
#plot a linear the fitting linear function
def plot (x,y,dx,dy,a,b,x_axis_title,y_axis_title):
    #error ploting
    error = plt.errorbar(x, y, dx, dy, '+')
    plt.setp(error, color='b', linewidth=2.0, )

    #find and plot the fitting linear line
    yfit = [b + a * xi for xi in x]
    line = plt.plot(x, yfit)
    plt.setp(line, color='r', linewidth=2.0,)

    #axis title
    plt.xlabel(x_axis_title)
    plt.ylabel(y_axis_title)

    plt.show()

#calling the needed functions
def fit_linear(filename):
    x, y, dx, dy, x_axis_title, y_axis_title = input_handling(file_name)
    a, b = calculations(x, y, dx, dy)
    plot(x, y, dx, dy, a, b, x_axis_title, y_axis_title)

import matplotlib.pyplot as plt
file_name=input("please input the file name:")
fit_linear(file_name)