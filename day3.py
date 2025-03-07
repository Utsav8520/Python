#OOP in python
class person():
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
    def __str__(self):
        return f"{self.name}"
        
person1=person("utshav",21)
print(person1,person1.age)
            
            
#inheritence

class person():
    def __init__(store, name, age):
        store.name=name
        store.age=age
        
    def __str__(store):
        return f"{store.name}"
    
class Student(person):
    
    def __init__(store,name,age,roll):
        super().__init__(name,age)
        store.roll=roll
            
    def __str__(store):
        return f"{store.roll}"
            
person1=person("uthsav",22)
student1=Student("utshav",22,30)
print(person1,student1)


#Exception and Error Handling

            
            
            
    
    
        