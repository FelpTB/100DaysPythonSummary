programming_dictionary = {
    "Bug":"An error in a program thats prevents a code from runing as expected.",
    "Function":"A piece of code that you can easily call over and over again.",
    "Loop":"The action of doing something over and over again",
}
print(programming_dictionary["Bug"])

programming_dictionary["Variable"] = "A value that can be modified along the code"
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

capitals = {
    "France":"Paris",
    "Germany":"Berlin",
}

travelLog ={
    "France": ["Paris", "Lillie", "Dijon"],
    "Germany":{"Berlin": 4,"Hamburg":2,"Stuttgart":[12,22,3]}
}

