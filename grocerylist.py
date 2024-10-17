import random

# Função para conseguir o primeiro item da lista
def firstitem(): 
    dryfood = ["farinha", "arroz", "feijão", "macarrão"]
    return random.choice (dryfood)

# Função para conseguir o segundo item da lista
def seconditem():
    dairy = ["óleo", "manteiga", "leite", "iogurte"]
    return random.choice (dairy)

# Função para conseguir o terceiro item
def thirditem():
    meat = ["frango", "carne", "peixe", "ovos"]
    return random.choice (meat)

# Função para conseguir o quarto item
def fourthitem():
    seasoning  = ["sal", "pimenta", "vinagre", "salsa"]
    return random.choice (seasoning)

# Função de criação da lista
def get_list():
  
  item1 = firstitem()
  item2 = seconditem()
  item3 = thirditem()
  item4 = fourthitem()

  list = f"{item1} {item2} {item3} {item4}"
  return list

if __name__ == "__main__":
   print(get_list())
