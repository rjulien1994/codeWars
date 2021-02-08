class Calculator(object):
    def evaluate(self, string):
        self.opOrder = {
            '+': lambda n1,n2 : n1+n2, '-': lambda n1,n2 : n1-n2,#the first operation found is 
            '*': lambda n1,n2 : n1*n2, '/': lambda n1,n2 : n1/n2}#the last to be perform
        #converts the str into float create multi D list to handle parenthese
        equation = self.parentheses([self.strToFloat(x) for x in string.split()])  

        return self.operations(equation)
    
    def parentheses(self, myList):
        lenL = range(len(myList)) #stores len of list for code clarity
        for i in lenL:  
            if myList[i] == "(":    #search for parenthese
                lastO = i
            elif myList[i] == ")":  #if ) then we have a ( prior or a syntax error
                newList = [myList[x] for x in lenL if x <= lastO or x > i]  #remove current interpretation
                newList[lastO] = myList[lastO+1:i]  #creates a list in our list to give priority to operation
                return self.parentheses(newList)    #repeat
        return myList   #once no more parenthese are found return list 

    def operations(self, myList):
        if type(myList) is not list:  #if not a list we are done
            return myList
        if len(myList) == 1:    #if list has 1 elem there is no operations on this lvl
            return self.operations(myList[0])   #removes layer

        for op, f in self.opOrder.items(): #we check for operator on layer
            if op in myList:               #if operator if run the function on the two list/value
                posOp = len(myList) - 1 - myList[::-1].index(op)    #makes sure "-" is perform in order
                return f(self.operations(myList[:posOp]), self.operations(myList[posOp+1:]))

    def strToFloat(self, strn):
        try:
            return float(strn)
        except:
            return strn


print(Calculator().evaluate("10 * 5 / 2"))
print(Calculator().evaluate("3 * 4 + 3 * 7 - 6"))
print(Calculator().evaluate("2 + 3 * 4 / 3 - 6 / 3 * 3 + 8"))
print(Calculator().evaluate("1.1 + 2.2 + 3.3"))
print(Calculator().evaluate("1 - 2 + 3 - 4 - 5 - 6"))
#print(type(2.3) == type(2))