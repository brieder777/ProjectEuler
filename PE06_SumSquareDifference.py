__author__ = 'Brian Rieder'

# Problem 6: Sum Square Difference

# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square
# of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the
# square of the sum.

# Answer: 25164150


def sum_of_squares(top_val):
    return sum(i**2 for i in range(0, top_val+1))


def square_of_sum(top_val):
    return (sum(range(1, top_val+1)))**2

print(square_of_sum(100) - sum_of_squares(100))