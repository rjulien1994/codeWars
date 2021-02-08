def alphabet_position(text):
    output = " ".join([str(ord(i.lower()) - ord("a") + 1) for i in text if i.isalpha()])
    return output

print(alphabet_position("The sunset sets at twelve o' clock."))