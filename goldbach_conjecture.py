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

    for i in range(5, 50):

        if isEven(i):
            num = i
            i_list = []
            for i in range(2, num):
                j = num - i
                # print(j)
                # print("num")
                # print(num)

                if isPrime(i) and isPrime(j):
                    print(j)
                    i_list.append(i)
                    print("num")
                    print(num)
                    print("answer")
                    print(i, j)
                    # print(i_list)
                    flag = True
                    break

                    if j in i_list:
                        # print(i_list)
                        pass
                    else:
                        # print("1else")
                        #print(i, j)
                        pass
                else:
                    #print(i, j)
                    # print("2else")
                    pass

        else:
            print("not Even")


if __name__ == "__main__":
    main()
