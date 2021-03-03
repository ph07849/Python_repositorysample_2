import random

roll =random.randint(1,6)

guess =int(input("Guess the dice roll:\n"))

if guess==roll:
    print("Correct!They rolled a"+str(roll))
else:
    print("Wrong! They rolled a "+str(roll))

print("The computer rolled a " + str(roll))


computer_choice = random.choice(['scissors','rock','paper'])

user_choice =input('Do you want rock,paper,or scissors?\n')

if computer_choice==user_choice:
    print("TIE")
elif user_choice=='rock'and computer_choice =='scissors':
    print("You won , the computer has "+ computer_choice)
elif user_choice=='paper'and computer_choice=='rock':
    print("You won , the computer has " + computer_choice)
elif user_choice=='scissors' and computer_choice=='paper':
    print("You won, the computer had" + computer_choice)
else :
    print('You lose :( Computer wins :)')

expenses =[10.50,8,5,9,10]
sum = 0

for x in expenses:
    sum =sum + x
print("You spent $", sum ," in the lunch "sep='')
