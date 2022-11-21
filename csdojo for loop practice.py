#This to get the list of all the factors of 3 and 5
total = 0
for i in range(1,100):
    if i % 3 == 0 or i % 5 ==0:
        print (i)


#This to get the sum of the factors of  3 and 5
total = 0
for i in range(1,100):
    if i % 3 == 0 or i % 5 ==0:
        total += i
print(total)


