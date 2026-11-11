product_1_code, product_1_units, product_1_value  = input().split() 
product_1_code = int(product_1_code)
product_1_units = int(product_1_units) 
product_1_value = float(product_1_value)

product_2_code, product_2_units, product_2_value  = input().split()
product_2_code = int(product_2_code)
product_2_units = int(product_2_units) 
product_2_value = float(product_2_value)

value_total = (product_1_units * product_1_value) + (product_2_units * product_2_value)

print(f"VALOR A PAGAR: R$ {value_total:.2f}")