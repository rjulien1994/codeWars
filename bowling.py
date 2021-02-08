def bowling_score(frames):
    frameList = [[shot for shot in frame[::-1]] for frame in frames.split()[::-1]]
    
    score = []
    total = 0
    if len(frameList[0]) == 3:
        for shot in range(3):
            if frameList[0][shot] == 'X':
                score.append(10)
                total += 10
            elif frameList[0][shot] == '/':
                score.append(10 - int(frameList[0][shot+1]))
                total += 10 - int(frameList[0][shot+1])
            else:
                score.append(int(frameList[0][shot]))
                total += int(frameList[0][shot])
        del frameList[0]
    
    frameList = [x for elem in frameList for x in elem]

    for i in range(len(frameList)):
        if frameList[i] == 'X':
            score.append(10)
            total += sum(score[-3:])
        elif frameList[i] == '/':
            score.append(10-int(frameList[i+1]))
            total += sum(score[-2:])
        else:
            score.append(int(frameList[i]))
            total += score[-1]
        

    return total

print(bowling_score('5/ 6/ 22 10 01 1/ 6/ 33 X 5/3'))