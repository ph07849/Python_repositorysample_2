
#This is a code for calculating all the basic Math operations
#Here we are creating a Main class or Blueprint for calculating code
#In the Class we are letting the code know basic inputs and separate functions for each mathematical operation

class cal():
#This is a constructor function that gives a prerequisites for this class the basic input of two numbers
    def __init__(self,a,b) :
        self.a=a
        self.b=b
# The below are separate functions of adding , subtracting , Multiplication and division
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
# The below is checking the Type error for the math operation
        if not isinstance(a,int):
            raise TypeError("a is not a integer")
        if not isinstance(b,int):
            raise TypeError("b is not a integer")
# This is a value error valid only for multiplication and division -need to doublecheck
        if not isinstance(a==0,b==0):
            raise ValueError("Multiplication and division will be invalid,please enter some other number")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
Answer=cal(a,b)
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("The Answer for adding first and second number is : ",Answer.add())
    elif choice == 2:
        print(" The Answer for subtracting first and second number is ", Answer.sub())
    elif choice == 3:
        print("The Answer for multiplying first and second number is : ", Answer.mul())
    elif choice == 4:
        print("The Answer for dividing first and second number is: ", round(Answer.div(), 2))
    elif choice == 0:
        print("Exiting!")
    else:
        print("Invalid choice!!")

print()
print("The code execution is completed")
