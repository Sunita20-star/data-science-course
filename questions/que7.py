# Use the random module to write a function that returns a random password of length n.
import random
import string
def password(n):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) 
    for i in range(n))
    return password
length = int(input("Enter the length of the password: "))
print("Generated password is:",password(length))
