"""
Lab 7 question 5
gradient_optimize

return a point based on gradient function 
"""

def gradient_optimize(x0, gradient, step_factor, direction, iterations):
    x = x0
    
    for _ in range(iterations):
        x = x + direction * step_factor * gradient(x)
    
    return x

def f(x):
    return 1 - x ** 2

def f_prime(x):
    return -2 * x

x0 = 2
x_star = gradient_optimize(x0, f_prime, 0.1, 1, 250)
print(f"x* = {x_star:.2f}, f(x*) = {f(x_star):.2f}")