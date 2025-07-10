# pip
# pip --version
# pip install- | pip uninstall
# pip list
# pip show numpy

import numpy

import mypackage.arithmetics 
print(numpy.version.version)
numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))

import requests
response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
print(response)
print(response.status_code)
print(response.json())


# Arithmetics Package
from mypackage import arithmetics
print(arithmetics.sum_two_values(1, 4))

from myotherpackage import otherarithmetics
print(otherarithmetics.sum_two_values(1, 4))