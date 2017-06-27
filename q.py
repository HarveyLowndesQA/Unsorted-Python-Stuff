class Class1(Exception):
    pass

class Class2(Class1):
    pass

class Class3(Class1):
    pass

y = 2
for x in (Class3, Class2, Class1):
    try:
        x = 1/y
        y = y - 1
        raise x
    except(ZeroDivisionError):
        print("Massive")
        break
    except(Exception):
        print("Monty")
    finally:
        print("Python")