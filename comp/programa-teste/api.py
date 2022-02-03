import requests
import json

def nome(n):
    r = requests.get('https://pokeapi.co/api/v2/pokemon/'+n)
    data = r.json()["name"]
    return data.capitalize()

def tipo(n):
    r = requests.get('https://pokeapi.co/api/v2/pokemon/'+n)
    data = list()
    for aux in r.json()["types"]:
        data.append(aux["type"]["name"].capitalize())
    return data

def stats(n):
    r = requests.get('https://pokeapi.co/api/v2/pokemon/'+n)
    data = list()
    i = 0
    for aux in r.json()["stats"]:
        i = aux["stat"]["name"].capitalize()
        data.append({i:aux["base_stat"]})
    return data

def peso(n):
    r = requests.get('https://pokeapi.co/api/v2/pokemon/'+n)
    data = int(r.json()["weight"])
    data = round(data / 2.205,2)
    return data

while (True):
    print('Numero do pokemon a ser pesquisado ou s para sair')
    cont = True
    n = input()
    if n == "s":
        break
    elif int(n)>900:
        print ("escreva um numero de 1-900")
        cont = False
    while(cont):
        print (nome(n))
        print ("O que gostaria de saber?\nTipo  Stats   Peso\n(Responda com t/s/p)")
        s = input()
        if s == "t":
            print(*tipo(n), sep = ' e ')
        elif s == "s":
            print(stats(n), sep = ", ")
        elif s == "p":
            print(str(peso(n)) + "kg")
        else:
            print ("erro")
        
        print("saber mais algo desse pokemon?(s/n)")
        s = input()
        if s == "n":
            cont = False
