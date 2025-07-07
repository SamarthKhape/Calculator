import math
z = str(input("Enter Start : "))
while z == 'Start':
    print()
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
    print("12. Exit")

    a   = input("Enter Your Choice :")

    if a =="1":
        def add(b,c):
            b = float(input("Enter your First No. :"))
            c = float(input("Enter your  Second No. :"))
            print("Addition is :")
            return print(float(b+c))
        add(b ='',c = '')

    elif a == "2":
        def sub(d,e):
            d = float(input("Enter your First No. :"))
            e = float(input("Enter your second No. :"))
            print("Substraction is :")
            return print(float(d-e))
        sub(d = '', e = '')

    elif a == "3":
        def mul(f,g):
            f = float(input("Enter your First No. :"))
            g = float(input("Enter your Second No. :"))
            print("Multiplication is :")
            return print(float(f*g))
        mul(f = '', g = '')

    elif a == "4":
        def div(h,i):
            h = float(input("Enter your First No. :"))
            i = float(input("Enter your Second No. :"))
            print("Division is :")
            return print(float(h/i))
        div(h = '', i = '')

    elif a == "5":
        def mod(j,k):
            j = float(input("Enter your First No. :"))
            k = float(input("Enter your Second No. :"))
            print("Modulus is :")
            return print(float(j%k))
        mod(j = '',k = '')

    elif a == "6":
        def log_(l):
            l = float(input("Enter your No. :"))
            print("Log is :")
            return print(float(math.log(l)))
        log_(l = '')

    elif a == "7":
        def fact(m):
            m = int(input("Enter your No. :"))
            print("Factorial is :")
            return print(int(math.factorial(m)))
        fact(m = '')

    elif a == "8":
        def sq_root(n):
            n = float(input("Enter your No. :"))
            print("Square Root is :")
            return print(float(n**0.5))
        sq_root(n = '')

    elif a == "9":
        def cube_(o):
            o = float(input("Enter your No. :"))
            print("Cube is :")
            return print(float(o*o*o))
        cube_(o = '')

    elif a == "10":
        def cube_root(p):
            p = float(input("Enter your  No. :"))
            print("Cube Root is :")
            return print(float(p**(1/3)))
        cube_root(p = '')

    elif a == "11":
        def expo(q,r):
            q = float(input("Enter your No. :"))
            r = float(input("Enter your Power No. :"))
            print("Exponent is :")
            return print(float(q**r))
        expo(q = '', r = '')

    elif a == "12":
        def stop():
            print("Thank you for using our Calculator !!")
        stop()
        break    

    else:
        print("Operator not available !!")