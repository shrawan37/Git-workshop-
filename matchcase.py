#matchcase is just like switch case 
 
x = int(input("enter the variable of X:"))
#x is the variable to match 

match x :
    #if x is 0
    case 0:
        print("x is zero")
    case 1:
        print("x is 1 ")
    case 2:
        print("x is 2")


    case _ if x == 90:
        print("enter less than 90 ")
    case _ :
        print(x)