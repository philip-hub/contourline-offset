# import panadas as pd :( not installed on this, but would make this significantly easier

firstRow = [298.4, 299.0, 304.8, 306.8] # these values can be changed and more rows can be added, but must be added to the rows list
secondRow = [299.0, 302.8, 303.4, 305.9, 308.2]
scale = 50


rows = [firstRow, secondRow]
d = float(input("Find the offsets for a contour line put in the elevation"))

def findPoint(Y1, Y2, d, scale, c):
    #xOffset = (scale*(d-x1))/(x2-x1)
    yOffset = (scale*(d-Y1))/(Y2-Y1)
    print(" "+c+" :"+str(yOffset))

e = 0
for value in rows:
    i = 0
 
    for point in value:
       
        if d > point:
           
           
            if len(value) > i+1:
                if d < value[i+1]:
                    y2= value[i+1]
                    c ="Y"
                    findPoint(point, y2, d, scale, c)

       
            if len(rows) > e+1:
                x2List = rows[e+1]
                if d < x2List[i]:
                    x2 = x2List[i]
                    c ="X"
                    findPoint(point, x2, d, scale, c)
               
               
           
        i = i+1
    e = e + 1


e = 0

for value in rows:
    i = 0
 
    for point in value:
       
        if d > point:
           
           
     
       
            if len(rows) > e+1:
                x2List = rows[e+1]
                if d < x2List[i]:
                    x2 = x2List[i]
                    c ="X"
                    findPoint(point, x2, d, scale, c)
               
        i = i+1
    e = e + 1
