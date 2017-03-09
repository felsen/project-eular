"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

"""

Divisibility rules for Prime Factor:

[2, 3, 5, 7, 11, 13]

1. If the last number is divided by 2. Then 2 is the Prime Factor.

2. If the sum of all the number's divided by 3. Then 3 is the Prime Factor.

3. If the last digits is 5 or 0. Then 5 is the Prime Factor.

4. Multiply the last digit by 2. Subtract the doubled digit from the
rest of the number.If the answer is divisible by 7 with no remainder.
Then the 7 is the Prime Factor.

5. Add the 1st, 3rd, 5th, 7th, 9th,..etc(digits)
Add the 2ed, 4th, 6th, 8th, 10th,..etc(digits)
If the difference is 0 or divided by 11. Then 11 is the Prime Factor.

6. Multiply the last digit by 9.
Subtract the result from the rest of the number.
if the number is divisible by 13. Then 13 is the Prime Factor.

"""

"""from __future__ import division

number = 13195"""

"""
Rule No 1:

5 / 2 = 2.5

Two is not a Prime Factor.

"""


"""
Rule No 2:

1+3+1+9+5 = 19
19 / 3 = 6.33

Three is not a Prime Factor.

"""


"""
Rule No 3:

If the last digit is 5 or 0, then 5 is the Prime Number.

13195 last digit is 5.

Five is the Prime Factor.

"""


"""
Rule No 4:

Multiply the last digit by 2:

5 * 2 = 10

1319-10 = 1309

1309 % 7 == 0

Seven is the Prime Factor.

"""


"""
Rule No 5:

13195

1+1+5 = 7

3+9 = 11

7-11 = -4

4 % 11 == 0(False)

Eleven is Not a Prime Factor.

"""


"""
Rule No 6:

13195

5 * 9 = 45

1319 - 45 = 1274

1274 % 13 == 0

Thirteen is the Prime Factor.

"""


""" finding the prime numbers between 0, 100 """


def prime(number):
    """
    Find all the prime number's between 2 to 100.
    """
    prime_lst = []
    for num in range(2, number + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_lst.append(num)
    return prime_lst


def prime_method1(start, end):
    """
    Finding all the prime numbers between 2 to 100.
    """
    target, number = 0, range(start, end + 1)
    while number[target] < number[-1]:
        for each_num in number:
            if (each_num % number[target] == 0) and (
                    number[target] < each_num):
                number.remove(each_num)
        target += 1
    return number


def is_prime(num):
    """
    Find the given number is prime number or not.
    """
    prime_lst = prime_method1(2, num+1)
    result = False  # "{} not a prime number".format(num)
    if not (num in prime_lst):
        result = True  # "{} is prime number".format(num)
    return result


def prime_factor(num):
    """
    Prime Factor algorithm from:
    http://stackoverflow.com/questions/16996217/prime-factorization-list
    But Memory Error when we go for more then 10000.
    """
    prime_or_not = is_prime(num)
    primfac = []
    inc_d = 2
    if prime_or_not:
        while inc_d * inc_d <= num:
            while (num % inc_d) == 0:
                primfac.append(inc_d)
                num //= inc_d
            inc_d += 1
        if num > 1:
            primfac.append(num)
    return list(set(primfac))


if __name__ == "__main__":
    print(prime(1000))
    print(prime_method1(2, 1000))
    print is_prime(165)
    print prime_factor(2857)
    print prime_factor(19999)
