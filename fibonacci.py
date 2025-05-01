

#Python script to print first 100 fibonacci numbers
def fibonacci():
    x = 0
    y = 1
    for i in range(50):
        z = x + x
        print(z)
        x = y
        y = x