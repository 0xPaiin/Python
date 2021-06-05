print("Calculator")
print("Enter First input: ")
num1 = int(input())
print("Enter 2nd input: ")
num2 = int(input())
print("Enter Operator: " + "+, -, *, /, %, ** ")
num3 = input()
if num1 == 45 and num2 == 3 and num3 == "*" :
    print(int(555))
elif num1 == 56 and num2 == 9 and num3 == "+":
    print(int(77))
elif num1 == 56 and num2 == 6 and num3 == "/":
    print(int(4))
elif num3 == "+":
    add = num1 + num2
    print(int(add))
elif num3 == "-":
    subtract = num1 - num2
    print(int(subtract))
elif num3 == "*":
    multiply = num1 * num2
    print(int(multiply))
elif num3 == "/":
    devide = num1 / num2
    print(int(devide))
elif num3 == "%":
    quot = num1 % num2
    print(int(quot))
elif num3 == "**":
    squ = num1 ** num2
    print(squ)
else:
    print("Error in your input")
