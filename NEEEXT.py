friends = ["Toby", "Kelly", "Gege"]
friends.sort()
print(friends)

print(friends)

print("TUPLES")
coordinates = [(4,7), (9,0)]
coordinates[0] = 100
print(coordinates[0])

print("FUNCTIONS")
def say_hi(name):
    print("Hello " + name + " I Need to Drink Coffee")

print("Top")
say_hi("Inda")
say_hi("Lila")
print("Bottom")

print("RETURN STATEMENT")
def cube(num):
    return num*num*num

result = cube(4)
print(result)