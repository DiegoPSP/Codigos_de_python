#Calcular delta

a = float(input("Digite o valor de a: "))
b = float(input("Digite o vaor de b: "))
c = float(input("Digite o valor de c: "))

print(f"\nOs valores de A, B e C são respectivamente = {a}, {b}, {c}\n")
print("delta = b * b - 4 * a * c")

delta = (b ** 2) - (4 * a * c)
print("*****************************\n")
if a == 0:
    print("O valor de a não pode ser 0")
elif delta < 0:
    print("Não existe raizes reais!")
else:

    print(f"bhaskara_x1 = (-b + ({delta} ** (1/2)) / (2 * a)")
    print(f"bhaskara_x2 = (-b - ({delta} ** (1/2)) / (2 * a)")

    bhaskara_x1 = (-b + delta ** (1 / 2)) / (2 * a)
    bhaskara_x2 = (-b - (delta ** 0.5)) / (2 * a)
    print(f"\nO valor de X1 = {bhaskara_x1}\n O valor de X2 {bhaskara_x2}")
   
