import csv

class Point:
    def __init__(self, x_, y_):
        self.x=x_
        self.y=y_

class Line:
    def __init__(self, p_, q_):
        self.p=p_
        self.q=q_

class Nation:
    def __init__(self, name_, lines_):
        self.name=name_
        self.borders=lines_

def max(numOne, numTwo):
    if (numOne>numTwo):
        return numOne
    else:
        return numTwo

def min(numOne, numTwo):
    if (numOne< numTwo):
        return numOne
    else:
        return numTwo

def onSeg(p, q, r):
    if (q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y)):
        return True
    else:
        return False

def orientation(p, q, r):
    val=(q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    #print(val)
    if (val==0):
        return 0 #colinear
    elif (val>0):
        return 1
    elif (val<0):
        return 2

def check_intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    #print(o1,o2, o3, o4)
    #this part not right output
    if (o1 != o2 and o3 != o4):
        return 1
    elif (o1 == 0 and onSeg(p1, p2, q1)):
        return 2
    elif (o2 == 0 and onSeg(p1, q2, q1)):
        return 2
    elif (o3 == 0 and onSeg(p2, p1, q2)):
        return 2
    elif (o4 == 0 and onSeg(p2, q1, q2)):
        return 2
    else:
        return 0


def create_points(arr):
    points=[]
    for i in range(0, len(arr),2):
        x=float(arr[i])
        y=float(arr[i+1])
        #print(x,y)
        pt=Point(x, y)
        points.append(pt)
    return points

def create_lines(arr):
    lines=[]
    for i in range(len(arr)):
        if (i<len(arr)-1):
            ln=Line(arr[i], arr[i+1])
            #print(arr[i].x,arr[i].y, arr[i+1].x, arr[i+1].y)
            lines.append(ln)
        else:
            ln=Line(arr[i], arr[0])
            #print(arr[i].x,arr[i].y, arr[0].x, arr[0].y)
            lines.append(ln)
    return lines

def create_nation(arr):
    ind2remove=[0,0]
    name=arr[0]
    #print(name)
    for i in ind2remove:
        del arr[i]
    #print arr
    nation=Nation(name, create_lines(create_points(arr)));
    return nation
        
def check_nation(lines, p2, q2):
    intersect_c=0
    onSeg_=False
    for i in range (len(lines)):
        rt=check_intersect(lines[i].p, lines[i].q, p2, q2)
        #print(lines[i].p.x,lines[i].p.y, lines[i].q.x, lines[i].q.y)
        #input is wrong
        if(rt==1 or rt==2):
           intersect_c+=1
           if(rt==2):
              onSeg_=True
    if(onSeg_):
        return True
    elif(intersect_c % 2 == 0):
        return False
    else:
        return True

def main():
    
    all_check=False
    ot=Point(210, 202)
    nations=[]
    with open('nation.csv', 'r') as f:
        reader = csv.reader(f)

        for row in reader:
            nation=create_nation(row)
            nations.append(nation)
    
        
    input = []
    
    while True:
        line = raw_input("")
        if line:
            input.append(line)
        else:
            break
    text = ','.join(input)

    pts= create_points(text.strip().split(','))
    
    for i in range(len(pts)):
        all_check=False
        for j in range(len(nations)):
            if(check_nation(nations[j].borders, pts[i], ot)):
                print pts[i].x, ", " ,pts[i].y, " is inside ", nations[j].name, "\n"
                break
            elif(j==len(nations)-1):
                print pts[i].x, ", " ,pts[i].y, ", ", "is in open ocean" ,"\n"

if __name__ == "__main__":
    main()


