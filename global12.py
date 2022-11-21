#local scopes can't use Variables on Other Scopes
def spam(): 
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

#Global Variables can be read from a local scope

def spam():
    print(eggs)

eggs = 42
spam()
print(eggs)