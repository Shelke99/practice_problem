##WAP read an integer from the user and check whether the num is even or odd
num = int(input("enter the number:"))
if num // 2 and num % 2 == 0:
    print("the number is even:",num)

else:
    print("the number is odd:",num)