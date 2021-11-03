import pandas as pd

####################################
### Challenge 395 (Nonogram row) ###
####################################

# https://www.reddit.com/r/dailyprogrammer/comments/o4uyzl/20210621_challenge_395_easy_nonogram_row/

# A binary array is an array consisting of only the values 0 and 1. 
# Given a binary array of any length, 
# return an array of positive integers that represent the lengths of the sets of consecutive 1's 
# in the input array, in order from left to right.

test = []

def solver(input):
    df = pd.DataFrame({'vals':input})
    df['inverseVals'] = -(df['vals']-1)
    df['cumSum'] = df['inverseVals'].cumsum() * df['vals']

    dfSol = df.groupby('cumSum').agg({'vals':'sum'})

    return list(dfSol[dfSol['vals'] > 0]['vals'])

testList = [[0,0,0,0,0],
            [1,1,1,1,1],
            [0,1,1,1,1,1,0,1,1,1,1],
            [1,1,0,1,0,0,1,1,1,0,0],
            [0,0,0,0,1,1,0,0,1,0,1,1,1],
            [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]]

for i in testList:
    print(solver(i))