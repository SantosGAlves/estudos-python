name = str(input()) 
salary = float(input())
value_sold = float(input())  
OVER = 0.15


final_salary = salary + (value_sold * OVER)

print(f"TOTAL = U$ {final_salary:.2f}")