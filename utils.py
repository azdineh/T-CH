import random
def generateRandomNumber(numbers_of_digits=4):
    first_digit = str(random.randint(1, 9))
    remaining_digits = list(range(10))
    remaining_digits.remove(int(first_digit)) 
    selected_digits = random.sample(remaining_digits, numbers_of_digits - 1)
    result = first_digit + ''.join(map(str, selected_digits))
    return result