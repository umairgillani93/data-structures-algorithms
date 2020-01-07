# Reverse the words in sentences 
def reverse(sentence):
    return sentence.split()[::-1]

print(reverse('this is first sentence'))

def reverse1(sentence):
    sentence = sentence.split()
    
    if len(sentence) == 1:
        return sentence 

    else:
        return reverse1(sentence[1:]) + sentence[0]

print(reverse1('this is second sentence))