import math
import turtle
from turtle import *


def isEven(i):
    if i % 2 == 0:
        return True
        # print("helloworld")

    else:
        return False
        # print("helloworldd")


def isPrime(num):
    from math import sqrt
    if num == 0 or num == 1:
        flag = False
    elif num == 2:
        flag = True
    else:
        for i in range(2, num):
            if num % i == 0:
                #print("in loop")
                # print(i)
                flag = False
                break
            else:
                flag = True
    return flag


def isnum(string):
    if string.isdigit():
        return True
    else:
        return False


def main():
    i_list = []
    for i in range(5, 50):

        if isEven(i):
            num = i
            print(num)

            for i in range(1, num):
                j = num - i
                # print(j)
                # print("num")
                # print(num)

                if isPrime(i) and isPrime(j):
                    # print(j)
                    i_list.append(i)
                    # print("num")
                    # print(num)
                    print("answer")
                    print(i, j)
                    flag = True
                    break

                    if j in i_list:
                        pass
                    else:
                        # print("1else")
                        #print(i, j)
                        pass
                else:
                    #print("not prime")
                    pass

        else:
            # print(i)
            #print("not Even")
            pass


# taking input
number = turtle.textinput("user input", "enter a even number")

# print number input
print(number)

if __name__ == "__main__":
    main()
