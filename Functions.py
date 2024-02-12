# functions take argument and produce result (e.g. y=x)

# general form of python function is:
# def function_name(arguments):
#   {lines telling function what to do to produce result}
# return result

# producing a function that returns x^2 + y^2
def squared(x, y):
    result = x**2 + y**2
    return result


print(squared(16, 36))


# new function

def born(country):
    return print("I am from " + country)


born("England")
