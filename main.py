# Importing sympy library
import sympy as sp

# Defining the variable (symbol) x
x = sp.symbols('x')

# Example 1: Differentiation
# Function f(x) = x^2 + 3x + 5
func1 = x**2 + 3*x + 5
derivative_func1 = sp.diff(func1, x)
print("Derivative of f(x) = x^2 + 3x + 5:", derivative_func1)

# Example 2: Indefinite Integration
# Function f(x) = sin(x) + x^2
func2 = sp.sin(x) + x**2
integral_func2 = sp.integrate(func2, x)
print("Indefinite integral of f(x) = sin(x) + x^2:", integral_func2)

# Example 3: Definite Integration
# Definite integral of f(x) = sin(x) from 0 to pi
definite_integral_func2 = sp.integrate(sp.sin(x), (x, 0, sp.pi))
print("Definite integral of sin(x) from 0 to pi:", definite_integral_func2)

# Example 4: Second Derivative
# Function f(x) = x^3 + x^2
func3 = x**3 + x**2
second_derivative_func3 = sp.diff(func3, x, 2)
print("Second derivative of f(x) = x^3 + x^2:", second_derivative_func3)

# Example 5: Custom Expression (input function)
# Allowing the user to input a custom function
user_input = input("Enter a function of x (e.g., x**2 + sin(x)): ")
custom_func = sp.sympify(user_input)

# Differentiating the user input function
custom_derivative = sp.diff(custom_func, x)
print(f"Derivative of the function {user_input} is: {custom_derivative}")

# Integrating the user input function
custom_integral = sp.integrate(custom_func, x)
print(f"Indefinite integral of the function {user_input} is: {custom_integral}")

# Example 6: Solving Definite Integral for User Input (Range 0 to 2)
custom_definite_integral = sp.integrate(custom_func, (x, 0, 2))
print(f"Definite integral of {user_input} from 0 to 2 is: {custom_definite_integral}")