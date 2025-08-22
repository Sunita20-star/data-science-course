
def square_root(number):
    if number < 0:
        return "Square root of negative numbers is not supported."
    if number == 0 or number == 1:
        return number
    guess = number / 2.0  
    for i in range(20):  
        guess = (guess + number / guess) / 2.0
    return guess
