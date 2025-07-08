import my_module
my_module.sum(5, 3, 1)
my_module.print_value('Byee')

from my_module import sum, print_value
sum(1, 2, 3)
print_value('Hellooo')

import math
print(math.pi)
print(type(math.pi))
print(math.pow(2, 8))

from math import pi as PI_VALUE
print(PI_VALUE)
