i = 0

def findPoint(Y1, Y2, d, scale, c, fileName):
  #xOffset = (scale*(d-x1))/(x2-x1)
  if Y1 < Y2:
    if d > Y1 and d < Y2:
      yOffset = (scale*(d-Y1))/(Y2-Y1)
      equation = str(scale)+"*("+str(d)+" - "+str(Y1)+" )/("+str(Y2)+" - "+str(Y1)+")"
      print(" "+c+" :"+str(yOffset))
      print(equation)
      offScale = round(yOffset,-1)
      print(" Offset Scaled "+str(offScale))
      with open(fileName, 'a') as f:
          f.writelines("Next Equation\n")
          f.writelines("Equation: "+equation+"\n")
          f.writelines("Answer: "+str(yOffset)+"\n")
          f.writelines("Answer on Scale: "+str(offScale)+"\n\n")
    else:
      print("Recheck if this Line goes in")
  if Y2 < Y1:
    if d > Y2 and d < Y1: 
      yOffset = (scale*(d-Y2))/(Y1-Y2)
      equation = str(scale)+"*("+str(d)+" - "+str(Y2)+" )/("+str(Y1)+" - "+str(Y2)+")"
      print(equation)
      print(" "+c+" :"+str(yOffset))
      offScale = round(yOffset,-1)
      print(" Offset Scaled "+str(offScale))
      with open(fileName, 'a') as f:
          f.writelines("Next Equation\n")
          f.writelines("Equation: "+equation+"\n")
          f.writelines("Answer: "+str(yOffset)+"\n")
          f.writelines("Answer on Scale: "+str(offScale)+"\n\n")

    else:
      print("Recheck if this Line goes in")

while i ==0:
    scale = 100
    dp = float(input("Enter in the desired contour line\n"))
    fileName = str(dp)+"countour.txt"
    x1 = float(input("Enter in p1\n"))
    x2 = float(input("Enter in p2\n"))
    # y1 = input("Enter in y1\n")
    # if y1 != "c":
    #   y1 = float(y1)
    #   y2 = float(input("Enter in y2\n"))
    #   findPoint(x1, x2, dp, scale,"x", fileName)
    #   findPoint(y1, y2, dp, scale,"y", fileName)

    # if y1 != x1 and y1 !="c":
    #     print("problem recheck coords")
    
    # if y1=="c":
    # coor = input("what axis\n")
    coor = "stm" #speed type mode
    findPoint(x1, x2, dp, scale,coor, fileName)
    
