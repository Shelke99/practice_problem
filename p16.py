# read an integer from the user and print a small number if the number is less than 100 and  print large  number if number is greater than
# 200 print the very larg number if the number is greater then 1000
num = int(input("enter the number:"))
if num < 100:
    print("number is small", num)
elif num > 1000:
    print("number is very large:", num)
elif num > 200:
    print("number is large", num)
