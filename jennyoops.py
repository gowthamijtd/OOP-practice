#Practice
class Instructor:
    followers=0  #class object variable
    def __init__(self,instructor_name,address,):
        self.name=instructor_name
        self.address=address
        #self.followers=0
        #expect subject_name string
    def Display(self,subject_name):
        print(f"Hi,I am {self.name} and I teach {subject_name}")
    def update_followers(self,follower):     
        self.followers +=3
instructor_1=Instructor("jenny","Delhi")
print(instructor_1.name)
instructor_1.Display("Python")
print(instructor_1.address)
print(instructor_1.followers)
instructor_1.update_followers("hari")
print(instructor_1.followers)
instructor_2=Instructor("Gowthami","Andhrapradesh")
print(instructor_2.name)
print(instructor_2.address)
print(instructor_2.followers)
instructor_2.update_followers("hema")
print(instructor_2.followers)

print("=================================================================")

#EXERCISE:
class Circle:
    pi=3.14  #class object Attribute
    def __init__(self,radius):
        self.r=radius
    def area(self,radius):
        a=self.pi*(self.r)**2
        return a
    def circumference(self,radius):
        b=2*self.pi*self.r
        return b
circle_1=Circle(4)
print("area of circle_1 is:",circle_1.area(3))
print("circumference of circle_1 is:",circle_1.circumference(3))
circle_2=Circle(3)
print("area of circle_2 is:",circle_2.area(3))
print("circumference of circle_2 is:",circle_2.circumference(3))

print("====================================================================")

#EXERCISE
class Rectangle:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def perimeter(self,l,b):
        c=2*(self.l+self.b)
        return c
    def area(self,l,b):
        d=self.l*self.b
        return d
rectangle_1=Rectangle(4,2)
print(f"perimeter of rectangle_1 is:{rectangle_1.perimeter(4,2)}")
print(f"area of rectangle_1 is:{rectangle_1.area(4,2)}")
rectangle_2=Rectangle(5,3)
print(f"perimeter of rectangle_2 is:{rectangle_2.perimeter(5,3)}")
print(f"area of rectangle_2 is:{rectangle_2.area(5,3)}")

print("========================================================================")
           #single inheritance(one parent class,one child class)
#Practice                ##Inheritance example     (reusability of the code,we can create a new class from already existing class,we 
class Human:  #base class/parent class/super class                     #can inherit features and attributes from already created class )
    def __init__(self,num_heart):
        self.num_eyes=2  #super class attributes               
        self.num_nose=1
        self.num_heart=num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male(Human):  #child class/derived class/sub class
    def __init__(self,name,heart):
        super().__init__(heart)   #{use-super() function to access parent class attributes in child class 
        self.name=name       #if there are separate attributes to child class}
    def flirt(self):
        print("I can flirt")
    def work(self):
        print("I can code" )    #method overriding
        super().work()  #accessing super class attribute
    def display(self):
        print(f"Hi, I am {self.name} and I have {self.num_heart} heart.")
        
male_1=Male("aakash",1)
print(male_1.name)
male_1.eat()
male_1.work()
male_1.flirt()
print(male_1.num_eyes)
print(male_1.num_heart)
male_1.display()

print("===============================================================================================")
           # multiple inheritance(more than one parent class,one child class)
#Practice
class Human:    #base class/parent class/super class       #can inherit features and attributes from already created class )
    def __init__(self,num_heart):
        print("calling init from Human")
        self.num_eyes=2  #super class attributes               
        self.num_nose=1
        self.num_heart=num_heart
    def eat(self):
       print("I can eat")
    def work(self):
       print("I can work")
        
class Male:     #2nd parent class
    def __init__(self,name):
        print("Calling init from male")
        self.name=name
    def flirt(self):
        print("I can flirt")
    def work(self):
        print("I can code")

class Boy(Human,Male):        #child class
    def __init__(self,name,heart,language):
        Male.__init__(self,name)
        Human.__init__(self,heart)
        self.language=language
    def sleep(self):
        print("I can test")
    def work(self):
        print("I can test")
    def display(self):
        print(f"Hi,I am {self.name} and I work on the {self.language}")
        
boy_1=Boy("Rahul",1,"python")
print(boy_1.num_nose)
print(boy_1.num_heart)
print(boy_1.language)
boy_1.display()
#boy_1.flirt()
#boy_1.work()
#print(Boy.mro())     #method resolution order
#Male.work(boy_1)

print("======================================================================")
                 # Multilevel inheritance(one parent class,one derived class,again derived class from derived class)
class Human(object):   #built-in class- object(parent class of all the classes)
    def __init__(self,num_heart):
        self.eyes=2
        self.heart=num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male(Human):
    def __init__(self,name):
        self.name=name
    def sleep(self):
        print("I can sleep whole day")
class Boy(Male):
    def work(self):
        #Human.work(self)
        super().work()
        print("I can code")
class Programmer(Boy):
    def work(self):
        print("I can write programs")
boy_1=Boy("Gowths")
boy_1.work()
print(boy_1.name)
print(Boy.mro())
prog_1=Programmer(1)
prog_1.work()


print("====================================================================")
                  #Hierarchical inheritance(one parent,more than one child)
class Human:
    def __init__(self,name,age):
        print("calling init from human class")
        self.name=name
        self.age=age
    def showDetails(self):
        print(f"name: {self.name},age: {self.age}")
    def eat(self):
        print("I can eat")
class Male(Human):
    def __init__(self,m_name,age,location):
        print("calling init from male class")
        Human.__init__(self,m_name,age)
        self.loction=location
    def sleep(self):
        print("I can sleep whole day.")
class Female(Human):
    def __init__(self,name,age,can_dance):
        print("Calling init from female class")
        super().__init__(name,age)
        self.know_dancing=can_dance
    def showDetails_F(self):
        Human.showDetails(self)
        print(f"know_dancing: {self.know_dancing}")
    def work(self):
        print("I can code")
female_1=Female("gowths",20,True)
female_1.eat()
female_1.showDetails_F()
print(female_1.age)
#male_1=Male("ram",34,'delhi')
#male_1.sleep()
#print(Male.mro())
        
print("====================================================================")
                        #Hybrid inheritance(combination of two or more inheritance)

class A:
    def display(self):
        print("display from A class")
class B(A):
    def display(self):
        print("display from B class")
class C:
    def show(self):
        print("Hi from C class")
class D(B,C):
    def display(self):
        print("display from D class")
d1=D()
d1.display()
print(D.mro())

print("====================================================================")
                 #Diamond problem
class A:
    def display(self):
        print("display from A class")
class B(A):
    pass
    # def display(self):
        #print("display from B class")  
class C(A):
    def show(self):
        print("Hi from C class")
    #def display(self):
     #   print("display from C class")   
class D(B,C):
    pass
    #def display(self):
       # print("display from D class")
d1=D()
d1.display()
print(D.__mro__)

print("=========================================================================")



    
