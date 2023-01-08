import math
import sympy
from sympy import *

number_of_success = int(input('Enter number of success x: '))
# 4
number_of_trials = int(input('Enter number of trials: '))
# 7

# define notations
x, n, p = symbols('x n p', real=True)
# define the function
func = (factorial(n) / (factorial((n-x)) * factorial(x))) * (p**x) * (1-p)**(n-x)
# take ln for both sides
ln_func = sympy.log(func, math.e)
# differentiate with respect p
derivative = diff(ln_func, p)
# subs with x and n from sample
derivative_sub = derivative.subs([(x, number_of_success), (n, number_of_trials)])
# Get maximum likelihood for p by solving equation for zero
p = solve(Eq(derivative_sub, 0), p)
print("value of parameter p: ", *p)
