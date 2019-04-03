equation = 'y = -12x + 11111140.2121'
list_equation = equation.split(' ')
x = 2.5
k = float(list_equation[2][0:len(list_equation[2]) - 1])
b = float(list_equation[3] + list_equation[4])
y = k * x + b
print(f'для x={x} у={y}')