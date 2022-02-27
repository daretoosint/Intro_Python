
print("LISTS")
friends = ["Pam" , "Toby" , "Michael" , "Jim"]
print(friends)
print(friends[0])
print(friends[1:])
print(friends[1:3])
friends[1] = "Phyllis"
print(friends[1])



print("LIST FUNCTIONS")
lucky_numbers = [4, 11, 13, 15, 20, 21, 22]
best_friends = ["Daffa", "Alma", "Alma", "Rara", "Zarra"]
best_friends.count("Alma")
print(best_friends)
best_friends.append("Creed")
best_friends.remove("Zarra")
best_friends.insert(1, "Kelly")
best_friends.extend(lucky_numbers)
print(best_friends)

print("DICTIONARIES")

monthConversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",

}
print(monthConversions["Mar"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Feb"))

print("WHILE LOOP")


