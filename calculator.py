#Calculator
print ("*" * 10, "Calculator", "*" * 10)
print ("Enter q to quit")
while True:
    s = input ("Put your operation sign (+,-,*,/): ")
    if s == "q": break # заканчивает выполнение программы
    if s in ("+", "-", "*", "/"):
        x = float (input("x = "))
        y = float (input("y = "))
        if s == "+":
            print ("%.2f" % (x+y))
        elif s == "-":
            print ("%.2f" % (x-y))
        elif s == "*":
            print ("%.2f" % (x*y))
        elif s == "/":
            if y != 0:
                print ("%.2f" % (x/y))
            else:
                print ("Can't divide by 0.")
        else:
            print ("Wrong operation sign.")