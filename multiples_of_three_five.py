# If we list all the natural numbers below 10 that are
# multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def main():
    multiplies_3 = range(0, 10)
    mul_3 = []
    for i in multiplies_3:
        if (i % 3 == 0) or (i % 5 == 0):
            mul_3.append(i)
    return sum(mul_3)


def method1():
    multiplies_5 = range(0, 1000)
    mul_5 = []
    for i in multiplies_5:
        if (i % 3 == 0) or (i % 5 == 0):
            mul_5.append(i)
    return sum(mul_5)


def method2():
    multiplies_5 = range(0, 1000)
    mul_5 = 0
    for i in multiplies_5:
        if (i % 3 == 0) or (i % 5 == 0):
            mul_5 += i
    return mul_5


if __name__ == '__main__':
    print main()
    print method1()
    print method2()

