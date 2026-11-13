valor = float(input())

valor = int(round(valor * 100))

print("NOTAS:")
notas = valor // 10000
print(f"{notas:.0f} nota(s) de R$ 100.00")
valor = valor % 10000

notas = valor // 5000
print(f"{notas:.0f} nota(s) de R$ 50.00")
valor = valor % 5000

notas = valor // 2000
print(f"{notas:.0f} nota(s) de R$ 20.00")
valor = valor % 2000

notas = valor // 1000
print(f"{notas:.0f} nota(s) de R$ 10.00")
valor = valor % 1000

notas = valor // 500
print(f"{notas:.0f} nota(s) de R$ 5.00")
valor = valor % 500

notas = valor // 200
print(f"{notas:.0f} nota(s) de R$ 2.00")
valor = valor % 200

print("MOEDAS:")

notas = valor // 100
print(f"{notas:.0f} moeda(s) de R$ 1.00")
valor = valor % 100

notas = valor // 50
print(f"{notas:.0f} moeda(s) de R$ 0.50")
valor = valor % 50

notas = valor // 25
print(f"{notas:.0f} moeda(s) de R$ 0.25")
valor = valor % 25

notas = valor // 10
print(f"{notas:.0f} moeda(s) de R$ 0.10")
valor = valor % 10

notas = valor // 5
print(f"{notas:.0f} moeda(s) de R$ 0.05")
valor = valor % 5

notas = valor // 1
print(f"{notas:.0f} moeda(s) de R$ 0.01")
valor = valor % 1
