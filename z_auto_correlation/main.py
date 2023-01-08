import numpy as np
import scipy.stats as stat
import math


def z_auto_corr(r: list, i: int, m: int, alpha: float):
    N = len(r)
    M = (N - m - i) // m
    nums_indx = [*range(i, N, m)]
    test_nums = np.array(r)[nums_indx]
    print("Test Numbers: ", test_nums)
    p_hat = (1 / (M + 1)) * sum(test_nums[:-1] * test_nums[1:]) - 0.25
    sigma_hat = math.sqrt(13 * M + 7) / (12 * (M + 1))
    z_0 = p_hat / sigma_hat
    print("Z0: ", z_0)
    z_c = stat.norm.ppf(1 - alpha / 2)
    print("Zc: ", z_c)
    if -z_c <= z_0 <= z_c:
        return "hypothesis h0 is not rejected"
    else:
        "hypothesis is rejected"


random_numbers = [0.12, 0.01, 0.23, 0.28, 0.89, 0.31, 0.64, 0.28, 0.83, 0.93,
                  0.99, 0.15, 0.33, 0.35, 0.91, 0.41, 0.60, 0.27, 0.75, 0.88,
                  0.68, 0.49, 0.05, 0.43, 0.95, 0.58, 0.19, 0.36, 0.69, 0.87]
# random_numbers = list(map(float, input("Enter random number: ").split()))
# alpha = float(input("Enter alpha: "))
# m = int(input("Enter Jump: "))
# i = int(input("Enter start index: "))

decision = z_auto_corr(random_numbers, 2, 5, 0.05)
print(decision)
