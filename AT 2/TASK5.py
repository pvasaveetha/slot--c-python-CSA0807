# Task 5: Functions, Parameters and Scope

def add_item_buggy(item, order=[]):
    order.append(item)
    return order


def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order


print(add_item_buggy("Tea"), add_item_buggy("Vada"))
print(add_item("Tea"), add_item("Vada"))


# Positional, keyword and default parameters

def order_details(item, quantity=1, price=10):
    total = quantity * price
    gst = total * 0.05
    return total, gst


print(order_details("Tea", 2, 15))
print(order_details(item="Coffee", quantity=3, price=20))


# Local variable

def local_example():
    x = 10
    print("Local:", x)

local_example()


# Global variable

x = 20

def global_example():
    global x
    x = 30

global_example()
print("Global:", x)


# Nonlocal variable

def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print("Nonlocal:", x)

outer()
