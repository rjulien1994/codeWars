def tickets(people):
    cash = { 25: 0, 50: 0, 100: 0}    #starting with 0 bills (100,50,25) 
    cost = 25
    for b in people:
        cash[b] += 1        #Receive payment
        change = b - cost   #compute change
    
        for i in range(0,2):    #always tries to give biggest bill
            bill = cost*(2**(1-i))
            while bill <= change and cash[bill] != 0:   #while because we might have to give multiple 25
                change -= bill  
                cash[bill] -= 1 #if we give the bill we dont have it anymore
        if change != 0: #checks that we could provide all the change
            return "NO"
    return "YES"
        
            

        
print(tickets([25,25,50]))