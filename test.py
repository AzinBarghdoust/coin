from threading import Timer, Event


def test(s, f):
    if s > f:
        print(True)
        return True
    else:
        print(False)
        return False


def test2():
    a = 15
    b = 20
    while a < 51:
        print(a)
        timer = Timer(5, test, args=(a, b))
        timer.start()
        a += 1
        if a > b:
            print(a)
            return a
        else:
            print(b)
            return b


timer = Timer(5, test2)
timer.start()