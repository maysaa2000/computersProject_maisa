file = open("errDataLength.txt","r")
data=file.readlines()
data_improved_1=[]
y_axis_title=data[len(data)-1]
x_axis_title=data[len(data)-2]
for line in data[:len(data)-2]:
    line_improved = line.strip('\n').lower().split()
    #print(line_improved)
    data_improved_1.append(line_improved)
print(data_improved_1)
row = len(data_improved_1)
colums=len(data_improved_1[0])
data_improved=[]
try:
 for c in range(colums):
        helper = []
        for r in range(row):
                helper.append(data_improved_1[r][c])
        #print(helper)
        data_improved.append(helper)
except:
 print(" Data lists are not the same length.")
 exit()
#print(data_improved)
for l in data_improved:
        axis = l[0]
        if axis == 'x':
                x = list(map(float, l[1:]))
        elif axis == 'y':
                y= list(map(float, l[1:]))
        elif axis == 'dx':
                dx = list(map(float, l[1:]))
        elif axis == 'dy':
                dy= list(map(float, l[1:]))
print(x)
print(dx)
print(y)
print(dy)
if len(x)!=len(y) and len(x)!=len(dy) and len(x)!=len(y):
    print(" Data lists are not the same length.")
    exit()
for test in dx :
    if test<=0:
        print( 'Not all uncertainties are positive.')
        exit()
for test in dy:
    if test<=0:
        print( 'Not all uncertainties are positive.')
        exit()
print("all ok")
