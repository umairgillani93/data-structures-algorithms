# Anagrams check 
def anagrams(str1, str2):

    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()

    return sorted(str1) == sorted(str2)

print(anagrams('abc','bca'))

# Another way (Brute-force method)
def anagrams1(str1, str2):
    
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()
    
    letter_dict = {}
    
    for letter in str1:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

    for letter in str2:
        if letter in letter_dict:
            letter_dict[letter] -= 1
        else:
            letter_dict[letter] = 1

    for k in letter_dict:
        if letter_dict[k] != 0:
            return False 

    return True 

print(anagrams1('clint eastwood', 'old west action'))