#WRITE YOUR CODE IN THIS FILE
def close10(x, y):
    if 10 - abs(x) < 10 - abs(y):
        return x
    elif 10 - abs(y) < 10 - abs(x):
        return y
    else:
        return 0
print(close10(5, 13))