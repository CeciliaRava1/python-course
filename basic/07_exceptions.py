# # Acceptance Criteria, not exception handling
# if type(numberTwo) == int:
#     print(numberOne + numberTwo)
# else:
#     print('No')

numberOne = 5
numberTwo = '1'

try: # Always execute
    print(numberOne + numberTwo)
    print('No error has occurred')
except:
    print('An error has occurred')
else: #(Optional)
    print('Execution continues correctly')
finally: # Always execute (Optional)
    print('Execution continues')

# Exceptions for type
try: 
    print(numberOne + numberTwo)
    print('No error has occurred')
except TypeError:
    print('A TypeError has occurred')
except ValueError:
    print('A ValueError has occurred')

# Capture info about exception
try: 
    print(numberOne + numberTwo)
    print('No error has occurred')
except ValueError as error:
    print(error)
except TypeError as error:
    print('A TypeError has occurred')