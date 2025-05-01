

#Python script to print first 100 fibonacci numbers
def fibonacci():
    x = 0
    y = 1
    for i in range(50):
        print(x)
        x,y = y,y+x
