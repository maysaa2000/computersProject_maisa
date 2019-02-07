def input_row (data):
    for line in data[0:len(data) - 2]:
        line_improved = line.strip('\n').lower().split()
        #print(line_improved)
        axis = line_improved[0]
        if axis == 'x':
            x = list(map(float, line_improved[1:]))
        elif axis == 'y':
            y = list(map(float, line_improved[1:]))
        elif axis == 'dx':
            dx = list(map(float, line_improved[1:]))
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



def input_colums(data):
    data_improved_1 = []
    for line in data[:len(data) - 2]:
        line_improved = line.strip('\n').lower().split()
        # print(line_improved)
        data_improved_1.append(line_improved)
    #print(data_improved_1)
    row = len(data_improved_1)
    colums = len(data_improved_1[0])
    data_improved = []
    try:
        for c in range(colums):
            helper = []
            for r in range(row):
                helper.append(data_improved_1[r][c])
            # print(helper)
            data_improved.append(helper)
    except:
        print(" Data lists are not the same length.")
        exit()
    # print(data_improved)
    for l in data_improved:
        axis = l[0]
        if axis == 'x':
            x = list(map(float, l[1:]))
        elif axis == 'y':
            y = list(map(float, l[1:]))
        elif axis == 'dx':
            dx = list(map(float, l[1:]))
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

def input_handling(file_name):
    file = open(file_name)
    data = file.readlines()
    axis_list = ['x', 'y', 'dx', 'dy']
    count = 0
    y_axis_title = data[len(data) - 1].strip('y axis :')
    x_axis_title = data[len(data) - 2].strip('x axis :')
    for axis in axis_list:
        if axis in data[0].lower():
            count += 1
    print(count)
    t = input_colums(data) if count == 4 else input_row(data)
    x, y, dx, dy = t
    return(t)


file_name = "working_colums.txt"
x=input_handling(file_name)
print(x)




