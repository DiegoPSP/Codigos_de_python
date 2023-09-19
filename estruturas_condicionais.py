MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))
#Condicionais apenas com "IF";
if idade >= MAIOR_IDADE:
    print("Você pode fazer o processo para tirar sua CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")

#Condicionais com "IF" e "ELSE", que resulta em 0 ou 1;
if idade >= MAIOR_IDADE:
    print("Você pode fazer o processo para tirar sua CNH.")
else:
    print ("Você não pode fazer o processo para tirar sua CNH.")

#Condicionais com "IF", "ELIF" (é uma maneira de proporcionar mais condições sem ser apenas falso como o else) e "ELSE";
if idade >= MAIOR_IDADE:
    print("Você pode começar a tirar sua CNH.")
elif idade == IDADE_ESPECIAL:
    print("Mas pode iniciar as aulas teóricas mas não pode fazer as aulas práticas.")
else:
    print("Não pode iniciar, pois não possui a idade mínima para fazer as aulas teóricas.")



