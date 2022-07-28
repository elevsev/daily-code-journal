def differentiation(y, x, p):
    '''First derivative of y'''
    y_diff = p * x ** (p - 1)

    return y_diff

x = 5
p = 2
y = x ** p

print(f"y = x: {x} ** p: {p} = {y}")
print(f"Derivative of y = p * x ** (p-1): {differentiation(y, x, p)}")