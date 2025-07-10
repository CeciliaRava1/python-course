### lambdas ###

sum_two_values = lambda number_one, number_two: number_one + number_two
print(sum_two_values(2, 4))

multiply_values = lambda number_one, number_two: number_one * number_two - 3
print(multiply_values(2, 4))

def sum_three_values(value):
    return lambda number_one, number_two: number_one + number_two + value


print(sum_three_values(5)(2, 4))