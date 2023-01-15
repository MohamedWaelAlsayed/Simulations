import sympy as smp

"""
Author : mohamed wael Alsayed
email : mohamed.wael.elsuid@gmail.com
"""

# Replace incorrect random number 18 with 28 for x
# Replace incorrect random number 100 with 0 for y
random_numbers = [22, 57, 25, 18, 28, 0, 45, 90, 25, 5, 27, 77, 48, 66, 43, 10, 40, 76, 47, 42, 38, 78, 33, 88, 24, 3,
                  47, 9, 42, 77, 25, 61, 33, 27, 50, 60, 34, 29, 21, 40]
# take random numbers from user
# random_numbers = list(map(int, input("Enter Random Numbers: ").split()))
# print(random_numbers)

iterations = int(input('Enter number of Iterations: '))

x_one = 2
x_two = 5

y_one = 0
y_two = 140

Area = (x_two - x_one) * (y_two - y_one)
# print(Area)

M = 0
N = 0

x_coordinate = 0
y_coordinate = 0
x_3 = 0


def polynomial(x: [int, float]):
    """Return x to the power of 3"""
    return x ** 3


j = 0

for i in range(iterations):
    # print("x : ", i, " , X^3 : ", polynomial(i))
    # print((random_numbers[j] >= x_one * 10))
    # print(random_numbers[j] <= x_two * 10)
    if (random_numbers[j] >= x_one * 10) and (random_numbers[j] <= x_two * 10):
        x_coordinate = round(random_numbers[j] * 0.1, 2)
    else:
        print(f"Random number of x: {random_numbers[j]} not in range (20,50)")
        break

    j += 1
    y_coordinate = round(random_numbers[j] * 0.01 * (y_two - y_one), 2)
    x_3 = round(polynomial(x_coordinate), 2)
    if y_coordinate <= x_3:
        M += 1
    N += 1
    print("Random Number for X: ", round(random_numbers[j - 1], 2), " X Coordinate: ", x_coordinate,
          " Random Number of Y: ",
          round(random_numbers[j] * 0.01, 2), " Y Coordinate: ", y_coordinate, " X^3: ", x_3,
          " M: ", M, " N: ", N)
    j += 1

# Calculate Integration Value using Monte Carlo
MonteCarlo_Value = (M / N) * Area

# Calculate Exact Integration and compare with monte carlo solution

exact_integration = smp.integrate(smp.Symbol("x") ** 3, (smp.Symbol("x"), 2, 5))
exact_integration = float(exact_integration)

print("#" * 50)
print("The real value of the integral is: ", exact_integration)
print("I: ", MonteCarlo_Value)
print("Error: ", abs(MonteCarlo_Value - exact_integration))