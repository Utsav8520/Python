#Global and local variables

a="This is a global variable"
def var():
    b="this is a local variable"
    print(b)
    
var()
print(a)

#Indexing and slicing
c="Utshav"
print(type(c))
print(c[5])
#To display required alphabets
print(c[1:5])

#concatenation
d="utshav"
e="satyal"
f=d+e
print(f)


#F-string : adds the string as well as variables
g="cipes"
h="limbu"
print(f"Whats up {g} {h}")

#Boolean
is_raining=False
if is_raining:
    print("Carry an Umbrella")
else:
    print("dont")
    
    #mod

#program to ask the user for number of people, total cash, and tip in percentage and to divide the cash equally among the people at last 
#people=int(input(" Enter the number of people"))
#Amount=int(input(" Enter the number of amount"))
#Tip_in_percentage=float(input(" Enter the tip in percentage"))
#Tip_in_number=(Tip_in_percentage/100*Amount)
#Divided_amount=(Tip_in_number*people+Amount)/people
#print(Divided_amount)






