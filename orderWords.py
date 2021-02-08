def order(sentence):
    words = sentence.split()    #separate the sentence into words
    newSentence = [None] * len(words)   #assign space for new sentence stucture (faster than assigning as you go)
    for w in words:  #split sentence into words
        for char in w:  #Since we don't know where the digit is but know there is only one per word
            if char.isdigit():  #fetch the position of the word in sentence
                newSentence[int(char)-1] = w #place word at appropriate position
    return " ".join(newSentence)    #concatonates the words into a sentence

print(order("is2 Thi1s T4est 3a"))