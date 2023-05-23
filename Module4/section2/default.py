def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)


introduction("James", "Doe")

introduction(last_name="Henry")


def add_numbers(a, b=2, c=3):
    print(a + b + c)


add_numbers(a=1, c=3)
