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


def main():

    for i in range(5, 11):

        if isEven(i):
            num = i
            i_list = []
            for i in range(1, num):
                j = num - i
                print(j)
                print(num)

                if isPrime(i) and isPrime(j):
                    print("answer")
                    print(i, j)
                    i_list.append(i)
                    # print(i_list)

                    if j in i_list:
                        # print(i_list)
                        pass
                    else:
                        print("answer")
                        print(i, j)
                else:
                    print(i, j)
                    print("1else")

        else:
            print("not Even")


if __name__ == "__main__":
    main()
