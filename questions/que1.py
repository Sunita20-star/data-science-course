n = 153
total = 0
temp = n

while temp > 0:
    digit = temp % 10
    total = total + digit**3
    temp //= 10

print('The sum of cubes of digits is', total)
print('Armstrong' if total == n else 'Not Armstrong')
