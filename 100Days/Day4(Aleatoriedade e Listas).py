import random
import myModule

print(myModule.pi)

random_int = random.randint(1,10)   #Gera um número aleatório entre 1 e 10(int)
print(random_int)

randomFloat = random.random()       #Gera um número aleatório entre 0 e 1(float)
randomFloat5 = random.random()* 5   #Gera um número aleatório entre 0 e 5(float)
print(randomFloat5)

fruits = ["Cherry", "Apple", "Pear"]
print(fruits[0])  #Primeiro
print(fruits[1])
print(fruits[-1]) #Ultimo
print(fruits[-2])

fruits.append("Pineaple") #Adiciona no final

fruits.extend(["Strawberry","Blueberry","Raspberry"]) #Adiciona um lista na lista

#print(fruits)

vegetables =["Spinach","Kale", "Tomatoes", "Celery", "Potatoes"]

plants = [fruits,vegetables]

print(plants)
print(vegetables.index("Kale")) #Retorna o índice do parâmetro na lista passada.