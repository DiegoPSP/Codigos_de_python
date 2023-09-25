name, age = "Diego", 21;
#variáveis podem ser criadas na mesma linha, é só seguir a ordem de atribuição;

print("O {name} possui {age} anos de idade.".__format__)
#para fazer a chamada de variáveis/constantes dentro do print deve-se colocar {} e tambem a letra "f" encostada nas aspas no inicio; 
# ou .__format__ no final, precisa de um ponto final antes da chamada;

#name = "Alan"
#print(f'O {name} possui {age} anos de idade.')

limite_saque_diario = 1000
#Nao abreviar nomes de variáveis ou colocar apenas caracteres soltos;

BRAZILIAN_SOUTHEAST_STATES = ["MG", "ES", "RJ", "SP"]
#Definição de constantes coloca com letras maiúsculas, porém podem ser alteradas também;

print(f"O {name} é um brasileiro. Ele nasceu em um estado do sudeste do Brasil, sendo que essa região possue essas siglas {BRAZILIAN_SOUTHEAST_STATES} com seus respctivos estados")
