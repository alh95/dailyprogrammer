import pandas as pd

########################################
### Challenge 399 (Letter Value Sum) ###
########################################

# https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/

# Assign every lowercase letter a value, from 1 for a to 26 for z. 
# Given a string of lowercase letters, find the sum of the values of the letters in the string.
#e.g. "" = 0, "a" = 1, "cab" = 3 + 1 + 2 = 6

def lettersum(string):
    string = string.lower() #ensure only lower case being used
    
    strsum = 0 #initialises the sum at zero
    for letter in string:
        if letter == ' ':
            strsum += 0 #if whitespace, add 0
        else:
            strsum += ord(letter) - 96 #if character, add the value
            #this may cause issues if non-alphabetic character used
    #print("The lettersum of " + string + " is: " + str(strsum))
    return(strsum)

## Bonus Challenge 1
# microspectrophotometries is the only word with a letter sum of 317. 
# Find the only word with a letter sum of 319.

words = pd.read_csv('enable1.txt', header = None).dropna() # read in document of words
words.columns = ['word']
words['length'] = words['word'].str.len() #add column to sort on length of words

words = words.sort_values(by = ['length','word'], ascending = [False, False])

max_length = 0

for word in words['word']:
    max_length = lettersum(word)
    if max_length == 319:       
        print('The word with lettersum 319 is: ' + word)
        break

## Bonus Challenge 2
# How many words have an odd letter sum?

words['lettersum'] = words['word'].apply(lettersum) #apply the lettersum function to all words in the list
print(str((words['lettersum'] % 2 == 1).sum()) + " words have an odd letter sum")

## Bonus Challenge 3
# There are 1921 words with a letter sum of 100, making it the second most common letter sum.
# What letter sum is most common, and how many words have it?

lettersumCount = words.groupby('lettersum').count()
maxCount = lettersumCount[lettersumCount['word'] == lettersumCount['word'].max()].index[0]
print(str(maxCount) + " is the most common lettersum")

## Bonus Challenge 4
# zyzzyva and biodegradabilities have the same letter sum as each other (151), 
# and their lengths differ by 11 letters. 
# Find the other pair of words with the same letter sum whose lengths differ by 11 letters.

words['plus11'] = words['length'] + 11
words['minus11'] = words['length'] - 11

for ls in list(lettersumCount.index):
    cut = words[words['lettersum'] == ls]
    if (cut['length'].isin(cut['plus11'])).sum() > 0:
        pair = list(cut[(cut['length'].isin(cut['plus11'])) | (cut['length'].isin(cut['minus11']))]['word'])
        print(pair, ' have the same letter sum ('  + str(ls) + ') and 11 difference in length')
    #could be a neater solution, but works

## Bonus Challenge 5
# cytotoxicity and unreservedness have the same letter sum as each other (188), 
# and they have no letters in common. 
# Find a pair of words that have no letters in common, 
# and that have the same letter sum, which is larger than 188. 
# (There are two such pairs, and one word appears in both pairs.)

for ls in list(lettersumCount.index):
    cut = words[words['lettersum'] == ls]