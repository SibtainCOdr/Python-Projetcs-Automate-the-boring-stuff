def zero(divideby):
    try:
        return 42 / divideby 
    except ZeroDivisionError:
        print("Error: invalid argument")

print(zero(2))
print(zero(12))
print(zero(0))
print(zero(1))
