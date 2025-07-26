#Read  a number if equal to  10 divide it by 2 , if the number if equal to 20 divide
#it by 3 if the number is equal to 30 divide it by 4  if the number if equal to 50 divided by 5 use switch case
num = int(input("enter a number: "))
result = 0
match num:
    case 10:
        result  = 10 / 2
    case 20:
        result = 20 / 3
    case 30:
        result = 30 / 4
    case 50:
        result = 50 / 5
print(result)





