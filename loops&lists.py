#loops
#A condition is satisfied 
number= 3 
while number <= 10:
    print("This is an infinite loop")
    number = number + 1
    #A certain amount of times

for i in range(5):
    print("This is iteration", i)
#Break and Continue
for i in range(6):
    if i == 3:
        break
    print("Inside Loop, iteration", i)
print("Outside Loop")

for i in range(6):
    if i == 3:
        continue
    print("Inside Loop, iteration", i)
print("Outside Loop")
#Lists
numbers=[1,2,3,4,5,6]
print(numbers)
print(numbers[2]) #to print a specific number from the array
print(numbers[-1]) #when using negative index, the counting of the position starts from the end
#if used alarger number in the brackets it will get out of range so it will be appeared as an error [8] for ex.

#Add and remove items from lists
#Append
numbers.append(7)
print(numbers)
#Insert
numbers.insert(2, 6)
print(numbers)
#Deleting items from lists
del numbers[2]
print(numbers)
