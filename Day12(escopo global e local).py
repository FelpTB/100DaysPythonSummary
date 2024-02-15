# enemies = 1
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")


##############local Scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
# drink_potion()
# print(potion_strength)

#############Global Scope

# player_health = 10
# def drink_potion():
#     global player_health
#     potion_strength = 2
#     player_health += potion_strength
#     print(player_health)

# def drink_potion2():
#     potion_strength = 2
#     print(potion_strength)
#     return player_health + potion_strength
    

# drink_potion()
# print(drink_potion2())


##########Blocks

# game_level = 3
# def create_enemie():
#     enemies = {"Skeleton", "Zombie", "Alien"}
#     if game_level <= 5:
#         new_enemie = enemies[0]

#     print(new_enemie)
# print(new_enemie)


################Global Constants

pi = 3.14159