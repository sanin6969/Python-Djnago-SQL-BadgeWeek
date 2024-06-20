# end parameters
# print('heloo' ,end =' ')
# print('world')

# sep parameters
# print('15','04','2003',sep='-')

#                                                       TODO: DATATYPES

#           TODO NUMERIC

# INTEGERS
# a=10
# b=-29
# c=6576565675675
# print(type(a),type(b),type(c))

# FLOAT
# a=109988.21
# b=-2567.776507786
# print(type(a),type(b))

#                   TODO sequence

# STRINgs slicing
# a='sanin'
# print(a[1:3])
# print(a[0:-4])
# print(a[::-2])

# list comprehension
# total=sum([x for x in range(1,10) if x%2==0])
# print(total)

# a=1,2,3,4,55,
# # print(type(a))

# a=((1,2),(3,4))
# print(a[0:2])

# Dict={}
# Dict = dict([(4, 'Rinku'), (2, 'Singh')]) 
# print('name:',Dict[4])
# print(Dict)


# def weekday():
#     day=int(input('enter a number between 1-7: '))
    
#     match day:
#         case 1:
#             print('MONDAY')
#         case 2:
#             print('TUESDAY')
#         case 3:
#             print('WEDNESDAY')
#         case 4:
#             print('THURSDAY')
#         case 5:
#             print('FRIDAY')
#         case 6:
#             print('SATURDAY')
#         case 7:
#             print('SUNDAY')
#         case _:
#             print('enter number between 1-7')
            
# weekday()
    
# def outerFunction(text): 
 
#     def innerFunction(text): 
#         print(text) 
 
#     # Note we are returning function
#     # WITHOUT parenthesis
#     return innerFunction  
# outerFunction('hey')

# y=10
# print('outside',y)
# def inner():
#     global y
#     y=y+1
#     x=5
#     print(x)
#     print(y)
# inner()
# print(y)

# x=1
# def outer():
#     x=2
#     def inner():
#         x=3
#         print('inner x:',x)
#     inner()
#     print('outer x:',x)
    
# outer()
# print('global x :',x)

# def b():
#     print('HHIIIIII') 
    
# a=b()
# a   
# def str_upper(func):
#     def uppper():
#         str1=func()
#         return str1.upper()
#     return uppper()
# @str_upper
# def print_str():
#     return 'gooood mooorninggg'

# print(print_str())

# TODO: two decorator in one function

# def upper_string(func):
#     def inner():
#         return func().upper()
#     return inner
# def split_string(func):
#     def inner():
#         return func().split()
#     return inner

# @split_string
# @upper_string
# def string():
#     return 'good moringgg guiys'

# print(string())

# a=[1,2,3,4,5]
# b=[]
# for i in a:
#     b.append(str(i))
# print(''.join(b))

# def outer(expr):
#     def inner(func):
#         return func()+ expr
#     return inner       
     
# @outer(' sanin')
# def string():
#     return 'good moringgg '

# print(string)

# class abc:
#     pass

# b=abc()
# print(type(b))

# class Student:
#     def __init__(self,name,batch,domain):
#         self.name=name
#         self.batch=batch
#         self.domain=domain
#     def display(self):
#         print('helloooo',self.name,'welcome')
        
# student_1=Student('sanin','21','python')
# print(student_1.name)
# student_1.display()

# TODO: single inheritance
# class Human:
#     def __init__(self,num_heart):
#         self.num_heart=num_heart
#         self.num_eyes=2
#         self.num_nose=1
    
#     def Work(self):
#         print('i can work')
        
#     def Eat(self):
#         print('i can eat')
        
# class female(Human):
#     def __init__(self,name,heart):
#         super().__init__(heart)
#         self.num_eyes=1
#         self.name=name
        
#     def clean(self):
#         print(' i can clean')
        
#     def Work(self):
#         Human().Work()
#         super().Work()
#         print('i can cook food')
        
# rani=female('rani',1)
# # rani.Work()
# print('name: ',rani.name)
# print('num of eyes:',rani.num_eyes)
# print('num of heart:',rani.num_heart)



# TODO: multiple inheritance
# class Human:
#     def __init__(self,num_heart):
#         self.num_heart=num_heart
#         self.num_eyes=2
#         self.num_nose=1
    
#     def Work(self):
#         print('i can work')
        
# class male():
#     def __init__(self,name):
#         self.name=name
        
#     def clean(self):
#         print(' i can clean')
# class boy(Human,male):
#     def __init__(self, age,heart,name):
#         Human.__init__(self,heart)
#         male.__init__(self,name)
#         self.age=age
#     def display(self):
#         print(f'hello am {self.name} and i have {self.num_heart} heart and my age is {self.age}')
        
        
# raju=boy(name='raju',age=21,heart=1)
# raju.display()

# TODO: access specifiers

class Branch:
    def __init__(self,name,rollno,age) -> None:
        self.name=name
        self._rollno=rollno
        self.__age=age
    def print(self):
        print(f'my name is {self.name} and my roll no is {self._rollno} and my age is {self.__age}')
        
b1=Branch('sanin',2,21)
b1.print()