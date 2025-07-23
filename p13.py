#find the largest number among the three num
max = 0
for i in range(0,3):
    i = int(input("enter the number:"))
    if max < i:
       max = i
print("the greater number is", max)
