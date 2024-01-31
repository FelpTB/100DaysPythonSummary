
def greet(name): #name = parametro
    print(f"Hello {name}")
    print("How you doin?")
    print("ins't the weather today?")
greet("Felipe") #Felipe = argumento

def greet2(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
greet2("Monsenhor Paulo" ,"Felipe") 
greet2(name="Felipe",location="Monsenhor Paulo")