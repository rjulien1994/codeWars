import numpy as np

def validate_battlefield(field):
    boats = [1,1,1,1,2,2,2,3,3,4]
    field = np.array(field)
    for row in range(10):
        for column in range(10):
            if field[row, column]:
                H, V = list(field[row:,column]), list(field[row,column:])
                H.append(0), V.append(0)
                H, V = H[:H.index(0)], V[:V.index(0)]
                lenH, lenV = len(H), len(V)
                if min(lenH, lenV) > 1: 
                    return False
                elif lenH == lenV: 
                    try:
                        boats.remove(1) 
                    except:
                        return False
                else:
                    try:
                        boats.remove(max(lenH, lenV))
                    except:
                        return False
                field[max(0,row-1):min(10, row+lenH+1), max(0,column-1):min(10,column+lenV+1)] = 0
    if boats:
        return False      
    return True

battleField = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                [1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],]

print(validate_battlefield(battleField))
