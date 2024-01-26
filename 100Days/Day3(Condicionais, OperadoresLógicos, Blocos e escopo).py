print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age in years? "))
    if age < 12:
        bill = 5
        print("Childs pay 5.")
    elif age <= 18:
        bill = 7
        print("Youths pay 7.")
    elif age >=45 and age <= 55:
        print("Everything is going ok, take a free ride.")
    else:
        bill = 12
        print("Adults pay 12.")
    foto = input("Do you want the photo taken? Y or N. ")

    if foto == "Y":
        bill += 3


    print(f"Please pay ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# == igual
# != diferente
# >= maior ou igual
# <= menor ou igual
# > maior
# < menor
    
# e == and
# ou == or
# não == not