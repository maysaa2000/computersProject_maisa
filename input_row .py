file = open("errSegma.txt","r")
data=file.readlines()
print(data)
y_axis_title=data[len(data)-1]
x_axis_title=data[len(data)-2]
#print(data)
for line in data[0:len(data)-2]:
    line_improved=line.strip('\n').lower().split()
    #print(line_improved)
    axis=line_improved[0]
    if axis=='x':
        x=list(map(float,line_improved[1:]))
    elif axis=='y':
        y=list(map(float,line_improved[1:]))
    elif axis=='dx':
        dx=list(map(float,line_improved[1:]))
    elif axis=='dy':
        dy=list(map(float,line_improved[1:]))
if len(x)!=len(y) and len(x)!=len(dy) and len(x)!=len(y):
    print(" Data lists are not the same length.")
    exit()
for test in dx :
    if test<=0:
        print( 'Input file error: Not all uncertainties are positive.')
        exit()
for test in dy:
    if test<=0:
        print( 'Not all uncertainties are positive.')
        exit()
print("all ok")
print(x,y,dx,dy)