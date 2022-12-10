from Triangle import *


def main():
    print("Length of the triangle : ")
    length = int(input())
    tr = Triangle(length)
    for i in range(20000):
        tr.addPoint()

    tr.trace()


main()
