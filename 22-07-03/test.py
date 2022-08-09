a, b = 3, 5


def add():
    global a, b
    a += 1
    b += 2


add()
print(a, b)
