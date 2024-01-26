#data Types
type(123)
type("123")
type(12.3)
type(True)

#String
print("Hello"[0])
print("123" + "345")

#Integer
print(123 + 345)

#123456789 = 123_456_789

#Float
print(123.456)

#Boolean
print(True, False)


#Conversão para string
#num_char = len(input("What is your name?"))
#new_num_char = str(num_char)
#print("Your name has " + new_num_char + " characters.")

a = str(123)
print(type(a))

print(70 + float(a))

#Operações
3 + 5 #Soma
7 - 4 #subtração
3 * 2 #Multiplicação
6 / 3 #Divisão
2 ** 3 #Potência

#PEMDAS () -> ** -> *  / -> +  -
#Prioridade
print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)

#Arredondar
print(8 / 3)
print(round(8/3))
print(round(8/3, 2))
print(8 // 3)

#Incrementar
i =+ 1
i = i + 1

#f-String
score = 6
height = 1.8
win = True
print(f"your score is {score}, your height is {height}, you are winning is {win}")

