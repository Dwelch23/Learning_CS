def add(num1, num2):
    return num1 + num2

sum = add(3, 4)
print(sum)

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(50))