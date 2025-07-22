# swapping two number without using third var
num1 = int(input('enter the integer number :'))
print("number_1 is:",num1)

num2 = int(input('enter the second number from the user:'))
print("number_2 is:",num2)

num1, num2 = num2, num1
print("number_1 is:",num1,"number_2 is:", num2)