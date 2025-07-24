# read an integer from the user and print a small number if the number is inbetween 100 and  200   print small number if number is in between 201 and 300 print big number
# and if number is in between 301 and 400 print large number  num is greater then 401 print the very large number
num = int(input("enter the number:"))
if 100 < num < 200:
    print("number is small", num)

elif 200 < num < 300:
    print("number is big:", num)
elif 300 < num < 400:
    print("number is large", num)
elif num < 401:
    print("number is very large", num)
#else:
    #print("number is very large", num)
