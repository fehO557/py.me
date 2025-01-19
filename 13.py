#calculo da hipotenusa do triângulo
import math
a = float(input("enter side A: "))
b = float(input("enter side B: "))
c = math.sqrt(pow(a, 2) + pow (b, 2))
print(f"The hipotenusa is: {round(c, 2)}")