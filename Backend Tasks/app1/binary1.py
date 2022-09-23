# Create a Python File
from math import *


def binary(num1, num2):
    b = ["", "", "", "", "", "", "", "", "", ""]
    c = ["", "", "", "", "", "", "", "", "", ""]
    d = ["", "", "", "", "", "", "", "", "", ""]
    l = 0
    binary_conversions = {

    }

    if num1 > num2:
        n1 = num1
        n2 = num2
    else:
        n1 = num2
        n2 = num1
    r = n2

    for n in range(n2, n1):
        i = n
        c[i - r] = n
        while n >= 1:
            b[i - r] = str(n % 2) + b[i - r]
            n = floor(n / 2)

        l = len(b[i - r])
        for j in range(0, l - 1):
            if b[i - r][j] == "1" and b[i - r][j + 1] == "1":
                binary_conversions[i] = True
                break
            else:
                binary_conversions[i] = False
    return binary_conversions

binary(2,7)

'''def fun(n1,n2):
    output={}
    for num in range(n1,n2):
        bin_num=bin(num).replace("0b","")
        if bin_num.find('11')!=-1:
            output[num]=True
        else:
            output[num]=False
    return output'''