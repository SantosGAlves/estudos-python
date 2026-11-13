
n = int(input())



horas = n // 3600
resto = n % 3600 

mins = resto // 60
resto = resto % 60

seg = resto

print(f"{horas}:{mins}:{seg}")

