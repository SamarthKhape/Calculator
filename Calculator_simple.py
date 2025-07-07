import math

print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Log")
print("7. Factorial")
print("8. Square Root")
print("9. Cube")
print("10. Cube Root")
print("11. Exponent")

a = input("Enter Your Choice :")

if a =="1":
    b = float(input("Enter your First No. :"))
    c = float(input("Enter your  Second No. :"))
    print("Addition is :")
    print(float(b+c))

elif a == "2":
    d = float(input("Enter your First No. :"))
    e = float(input("Enter your second No. :"))
    print("Substraction is :")
    print(float(d-e))

elif a == "3":
    f = float(input("Enter your First No. :"))
    g = float(input("Enter your Second No. :"))
    print("Multiplication is :")
    print(float(f*g))

elif a == "4":
    h = float(input("Enter your First No. :"))
    i = float(input("Enter your Second No. :"))
    print("Division is :")
    print(float(h/i))

elif a == "5":
    j = float(input("Enter your First No. :"))
    k = float(input("Enter your Second No. :"))
    print("Modulus is :")
    print(float(j%k))

elif a == "6":
    l = float(input("Enter your No. :"))
    print("Log is :")
    print(float(math.log(l)))

elif a == "7":
    m = int(input("Enter your No. :"))
    print("Factorial is :")
    print(int(math.factorial(m)))

elif a == "8":
    n = float(input("Enter your No. :"))
    print("Square Root is :")
    print(float(n*0.5))

elif a == "9":
    o = float(input("Enter your No. :"))
    print("Cube is :")
    print(float(o*o*o))

elif a == "10":
    p = float(input("Enter your  No. :"))
    print("Cube Root is :")
    print(float(p**(1/3)))

elif a == "11":
    q = float(input("Enter your No. :"))
    r = float(input("Enter your Power No. :"))
    print("Exponent is :")
    print(float(q**r))

else:
    print("Operator Not available !!!")