#Calcular delta

a = 2
b = 5
c = 2
print(f"\nOs valores de A, B e C são respectivamente = {a}, {b}, {c}\n")
print("delta = b * b - 4 * a * c")

delta = (5 * 5) - (4 * 2 * 2)
print(f"\nO valor de Delta é = {delta}\n")

print(f"bhaskara_x1 = (-b + ({delta} ** (1/2))) / (2 * a))")
print(f"bhaskara_x2 = (-b - ({delta} ** (1/2))) / (2 * a))")

bhaskara_x1 = (-5 + ({delta} ** (1/2))) / (2 * 2)
print(f"\nO valor de X1 = {bhaskara_x1}")

bhaskara_x2 = (-5 - (9 ** (1/2))) / (2 * 2)
print(f"\nO valor de X2 = {bhaskara_x2}\n")
