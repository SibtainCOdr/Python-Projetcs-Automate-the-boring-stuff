
def multi(num1, num2):
  
    
    product = num1 * num2

    if product <= 1000:
        return product
    else:
        return num1 + num2


result = multi(20, 30)
print('This is the result', result)

result = multi(40, 30)
print("The result is", result)