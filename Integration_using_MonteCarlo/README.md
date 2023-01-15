# Integration_using_MonteCarlo

## Use Monte Carlo method to evaluate the integral of a single variable polynomial function of x then compare i with exact value

This code is used to calculate the integration of a polynomial function (x^3) in a given range (2, 5).
It uses Monte Carlo integration technique to calculate the integration value.
The user is asked to enter a number of iterations and a list of random numbers.
The code then iterates through the list of random numbers and calculates the x coordinate, y coordinate, x^3, M and N values.
At the end, it calculates the Monte Carlo integration value and compares it with the exact integration value.
Finally, it prints out the real value of the integral, I (Monte Carlo Value), and Error (difference between Monte Carlo Value and Exact Integration Value).

## Time and Space Complexity

time complexity: O(n)

The space complexity: O(1)

## Libraries

 sympy

This code was a task in Simulations course (Semster 7 Fall 2022) in Faculty of computers and data science, Alexandria University
