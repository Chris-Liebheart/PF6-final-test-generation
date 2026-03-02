import requests
import json

def dish_fetch(num):
    """
    Recibe un número y retorna un diccionario con la información
    del plato correspondiente a ese índice en la API.
    """
    
    response = requests.get(f"https://api-colombia.com/api/v1/TypicalDish/{num}")
    typical_dish = json.loads(response.content)
    
    return typical_dish
def main():
 print("Hello, students!")
 user_dish = input("ingresa el numero del plato")
 print(dish_fetch(user_dish))
if __name__=="__main__":
 main()