import requests
import sys

cep = input("Digite o seu cep (sem pontuação): ")

if len(cep) != 8:
    sys.exit("CEP digitado inválido.")

get = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
json = get.json()

print(f"Para o cep {cep}, o logradouro é {json['logradouro']}, o bairro é {json['bairro']} e a cidade é {json['localidade']}")