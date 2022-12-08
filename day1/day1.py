

INPUT_FILE = "./input.txt"

total = 0
totals = list() 

with open(INPUT_FILE, "r") as f:
    for line in f:
        try:
            calories = int(line.strip())
            total += calories
        except ValueError:
            totals.append(total)
            total = 0

totals.sort()
print(f"Highest calories are: {totals[-1]} {totals[-2]} {totals[-3]}")   
 
print(f"Highest calories : {sum(totals[-3:])}")   
