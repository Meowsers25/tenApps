def recursion(num):
    if num == 1:
        return 1
    else:
        return num * recursion(num - 1)


print(recursion(4))
