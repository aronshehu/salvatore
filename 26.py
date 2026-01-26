#function
def function_name():
 print("Hello there")
function_name()
#parameters
def greeting(name):
    print("Hello",name)
greeting("Student")
#Keyword arguments
def sum(a,b,c):
   print(a)
   print(b+c)
sum(2,5,7) #also sum(b=2,a=5,c=7)
#Predefined argument values
def full_greeting(name, surname="Blank"):
   print("Hello", name, surname)
full_greeting("Student")
full_greeting("Good", "Student")
#Return values Instead of printing we can return as a value so we can use later on our program
def average(a,b,c):
   return (a+b+c)/3
avg = average(1,2,3)#you need to give a value
print("Your average value is:", avg)
#Scope changes made inside of function do not persist outside the function
x=0
def operation(x): #if we add a line global x all changes go to the previous x not the x in the way
   x+=1
   print(x)

operation (x)
operation(x)
print(x)
