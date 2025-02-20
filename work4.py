print("Hello world!!!")
date = '18.02.2025'


# x = 0
def outer():
    # global x
    x = 1
    def inner():
        nonlocal x
        x
    inner()
    print(x)

print(outer())