#Read  a number if equal to 10, 20, 30 divided by 2 if the number is equal to 40, 50  is divided by 3 use match case
num = int(input("enter the number:"))

match num:
    case 10|20|30:
        result = num / 2
    case 40|50:
        result = num / 3
    case _:
        result = "number is not handled"
print(result)