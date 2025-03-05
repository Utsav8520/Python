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







