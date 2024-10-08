import math
def p(x:int):
    return math.sqrt(x**3 -8)

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

    return

def trapazoid(tup: tuple[int, int, int]):
    dx = (tup[1]-tup[0])/tup[2]

    sum = 0
    for i in range(tup[2]):
        temp = p(tup[0]+ (i*dx))
        if i == 0 or i == tup[2]-1:
            temp*=2
        sum += temp

    sum/=2
    print("The trapazoid sum is:" + sum)
    return

def simpsons(tup: tuple[int, int, int]):

    return




def findSumMenu():
    tup = getParam()
    run = True
    while(run):
        num = input("What sum would you like to find:\n1.Midpoint\n2.Trapazoid\n3.Simpson's\n4.Left\n5.Right\n6.Exit\n")
        num = int(num)
        match num:
            case 1:
                midpoint(tup)
                break
            case 2:
                trapazoid(tup)
                break
            case 3:
                simpsons(tup)
                break




            case 6:
                return
            case _:
                print("Case \"" + num + "\" not recognized")
    return


def menu():
    run = True
    while(run):
        num = input("What would you like to do\n1.Enter Equation\n2.Check Equation\n3.Find Sum\n4.Exit\n")
        num = int(num)
        match num:
            case 1:
                enterEquation()
                break
            case 2:
                printEquation()
                break
            case 3:
                findSumMenu()
                break
            case 4:
                return
            case _:
                print("Case \"" + num + "\" not recognized")



if __name__ == "__main__":
    menu()

    