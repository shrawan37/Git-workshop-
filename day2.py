#this day is all about type casting 

#typecasting is the conversion of on data type into another datatype
#int() float() str() hex() oct() tuple() set() dict() etc 

a = "1" #string
b = "2" #string 
print(int(a)+int(b)) # this convert string 1 into int 1 


#two type of conversion is there 
#explict conversion (done by user)
#implict conversion (done by python automantically )

c = 1.9
d = 8 
print(c+d) #implict type casting example 

e = a+b
print(e)
print(type(e))