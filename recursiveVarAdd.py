#method 1

class add(int): #when the class is called it returns an int (has to be done when initializing)
    def __call__(self, n):  #the call function is when the class in called without attributes or methods
        return add(self + n)    #if called after initialization add vale to existing total

val = add(15)

print(val)