import math


def isEven(i):
    if i % 2 == 0:
        return True
        print("helloworld")

    else:
        return False
        print("helloworldd")


def isPrime(num):
    from math import sqrt
    if num == 0 or num == 1:
        flag = False
        print("if start")
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


def isnum(string):
    if string.isdigit():
        return True
    else:
        return False


def test():
    print("test works")


i_list = []
def main():

    test()

    for i in range(1, 11):

        if i % 2 == 0:
            num = i
            print(num)
            for i in range(1, num):
                j = num - 1
                print(j)
                print(num)

                if isPrime(i) and isPrime(j):
                    i_list.append(i)
                else:
                    print("helloworldd")

        else:
            print("helloworldd")


if __name__ == "__main__":
    main()
