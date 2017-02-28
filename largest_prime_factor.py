"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


number = 13195
div = [2, 3, 5, 7]
quocient = []

while number > 0:
    if number % div[0] == 0:
        number = number / div[0]
        quocient.append(div[0])
    elif number % div[1] == 0:
        number = number / div[1]
        quocient.append(div[1])
    elif number % div[2] == 0:
        number = number / div[2]
        quocient.append(div[2])
    elif number % div[3] == 0:
        number = number / div[3]
        quocient.append(div[3])


print quocient
