import math
import turtle
from turtle import *


def isEven(i):
    if i % 2 == 0:
        return True
    else:
        return False


def isPrime(num):
    from math import sqrt
    if num == 0 or num == 1:
        flag = False
    elif num == 2:
        flag = True
    else:
        for i in range(2, num):
            if num % i == 0:
                flag = False
                break
            else:
                flag = True
    return flag


def isNum(string):
    if string.isdigit():
        return True
    else:
        return False


def main():
    num = turtle.textinput("user input", "enter a even number")
    print(num)

    if isNum(num):
        num = int(num)
        if (num > 5) and isEven(num):
            i_list = []

            for i in range(1, num):
                j = num - i

                if isPrime(i) and isPrime(j):

                    i_list.append(i)
                    print("answer")
                    print(i, j)
                    flag = True
                    break

                    if j in i_list:
                        pass
                    else:
                        pass
                else:
                    pass

        else:
            print("Enter even number greater then 5")
            pass

    else:
        print("Enter a number")


if __name__ == "__main__":
    main()
