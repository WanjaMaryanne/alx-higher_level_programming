#!usr/bin/python3
for n in range(0, 10):
    for num in range(n + 1, 10):
        if n == 8 and num == 9:
            print("{}{}".format(n, num))
        else:
            print("{}{}".format(n, num), end=", ")
