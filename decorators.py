# Decorators are function that extends the behavior of another function w/o modifying the base function
# as an argument to the decorator.

def add_sprinkles(func):               # Here func = get_ice_creame python understands it by itself that they are equal .
    def wrapper():
        print('Adding Sprinkles ')
        func()
    return wrapper


@add_sprinkles
def get_ice_creame():
    print('Here is your ice creame 🍦🍧🍨')




get_ice_creame()