def create_phone_number(n):
    cond = all(num >= 0 and num < 10 for num in n) and len(n) == 10 #check that input is correct
    if not cond:
        return "Please verify input"    #if not ask user to verify input

    n = [str(num) for num in n]   #converts our int into strings 
    phoneNum = "({}) {}-{}".format("".join(n[:3]), "".join(n[3:6]), "".join(n[6:10]))  #create the format of phone num

    return phoneNum


print(create_phone_number([4, 5, 8, 9, 0,0,0,0,0,0]))
