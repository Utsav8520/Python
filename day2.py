#list
#make a list of people in the room and display using for loop

names=["nabin","ripes","utshav","giraffe"]
for n in names:
   print("hello "  + (n))
   
   #sorting
names.sort(reverse=True)
print(names)
    
    #tuple---immutable
    
a=("apple","banana")
a.pop()
    
a=["car","bike","car"]
print(a)
a.add("ballu")
print(a)
a.sort()
print(a)

#dictionaries

dict={
     "name":"utshav",
    "semester":"7th",
    "nested":{
        "abc":12
    }  
}
dict.update({"roll":21})
dict.pop("name")
dict.popitem()
print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict["sem"])

#functions

def fun(name):
    print(f"hello {name}")

fun("utshav")

name=["cipes","giraffe","nabin"]
def fun(name):
for x in name:
        print(f"hello {x}" )
        
        fun(name)
        
        
        #Task
        #--- list 5-10
        #--for loop
        #--create a list and print data using function
        #--bus  10>50,10-19=100,20-59=200,59>50, A/c: 50 
