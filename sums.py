import math

accuracy = 6

def p(x:int):
    return 9*math.cos((x**2))
#math.sqrt((x**3)-8)
#5*math.cos((x**2))

def enterEquation():
    return

def printEquation():
    return

def getParam() -> tuple[int, int, int]:
    a = int(input("Input lower bound:"))
    b = int(input("Input upper bound:"))
    n = int(input("Enter number of subdivisions:"))
    return (a,b,n)

def midpoint(tup: tuple[int, int, int]):
    dx = (tup[1]-tup[0])/tup[2]
    
    sum = 0
    for i in range(tup[2]):
        temp = p(tup[0]+(dx/2)+i*dx)
        sum += temp
        
    sum*=dx
    
    print("The midpoint sum is:\n" + str(rounding(sum)))
    
    
    
    return

def trapazoid(tup: tuple[int, int, int]):
    dx = (tup[1]-tup[0])/tup[2]

    sum = 0
    for i in range(tup[2]+1):
        temp = p(tup[0]+ (i*dx))
        if i != 0 and i != tup[2]:
            temp*=2
        sum += temp

    sum/=2
    sum*=dx
    print("The trapazoid sum is:\n" + str(rounding(sum)))
    return

def simpsons(tup: tuple[int, int, int]):
    if(tup[2]%2 == 1):
        print("Can not use simpsons with odd subdivisions!")
        return
    
    dx = (tup[1]-tup[0])/tup[2]
    
    sum = 0
    for i in range(tup[2]+1):
        temp = p(tup[0]+ (i*dx))
        if (i != 0 and i != tup[2]):
            if i%2 == 1:
                temp*=4
            else:
                temp*=2
        sum += temp
    
    sum*=dx
    sum/=3
    
    print("The simpson's sum is:\n" + str(rounding(sum)))
    return


def rounding(num:float):
    return round(num, accuracy)

def changeRounding():
    rounding = n if (n := input("What would you like rounding to be(current rounding is " + accuracy + ", enter -1 to cancle):")) <= -1 else rounding



def findSumMenu():
    tup = getParam()
    run = True
    while(run):
        num = input("What sum would you like to find:\n1.Midpoint\n2.Trapazoid\n3.Simpson's\n4.Left\n5.Right\n6.Back\n")
        num = int(num)
        match num:
            case 0:
                midpoint(tup)
                trapazoid(tup)
                simpsons(tup)
            case 1:
                midpoint(tup)
            case 2:
                trapazoid(tup)
            case 3:
                simpsons(tup)




            case 6:
                return
            case _:
                print("Case \"" + num + "\" not recognized")
    return


def menu():
    run = True
    while(run):
        num = input("What would you like to do\n1.Enter Equation\n2.Check Equation\n3.Find Sum\n4.Change Rounding\n5.Exit\n")
        num = int(num)
        match num:
            case 1:
                enterEquation()
            case 2:
                printEquation()
            case 3:
                findSumMenu()
            case 4:
                changeRounding()
            case 5:
                return
            case _:
                print("Case \"" + num + "\" not recognized")



if __name__ == "__main__":
    menu()

    