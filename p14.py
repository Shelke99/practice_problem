#Compute the Quotient and reminder of two number if b is non_zero
a = int(input("enter the number:"))
b = int(input("enter the number:"))

if b != 0:
    c = a // b
    print("the quotient is:", c)
    d = a % b
    print("the remainder is:", d)

