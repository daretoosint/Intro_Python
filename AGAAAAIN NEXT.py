print("IF STATEMENTS")

is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither a male nor tall")

a = 3
b = 2
if a < b:
    print ("a is less than b")
else:
    print("a is more than b")

c = 2
d = 3
if c < d:
    print ("c is less than d")
else:
    print("c is more than d")

e = 20
f = 8
if e < f:
    print("e is less than f")
elif e == f:
    print ("e is equal to f")
elif e > f + 10:
    print("e is greater than e more than 10")
else:
    print("e is greater than f")

g = 9
h = 8
if g < h:
    print("g is less than h")
else:
    if g == h:
        print("g is equal to h")
    else:
        print("g is greater than h")


name = "Inda"
height_m = 1.55
weight_kg = 45

bmi = weight_kg / (height_m * height_m)
print("bmi: ")
print(bmi)
if bmi < 25:
    print("Not overweight")
else:
    print("Overweight")


is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a male and also tall")
elif is_male and not(is_tall):
    print("You are a male but you are not tall")
elif not(is_male) and is_tall:
    print("You are not a male but you are tall")
else:
    print("You are not a male and also not tall hahahahaha")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(300, 40,5))

print("BUILDING A CALCULATOR, BTW YG DEFMAX ITU YG PALING LO GANGERTI YAK")

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print == (num1 * num2)
else:
    print("Invalid operator")
