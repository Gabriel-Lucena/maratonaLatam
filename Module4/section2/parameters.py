def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)


introduction(first_name="James", last_name="Bond")
introduction(last_name="Skywalker", first_name="Luke")


def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)


adding(c=1, a=2, b=3)

adding(3, c=1, b=2)

#Error

#adding(3, a=1, b=2)

