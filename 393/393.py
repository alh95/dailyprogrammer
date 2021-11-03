#####################################
### Challenge 393 (Making change) ###
#####################################

# https://www.reddit.com/r/dailyprogrammer/comments/nucsik/20210607_challenge_393_easy_making_change/

# The country of Examplania has coins that are worth 1, 5, 10, 25, 100, and 500 currency units. 
# At the Zeroth Bank of Examplania, 
# you are trained to make various amounts of money by using as many ¤500 coins as possible, 
# then as many ¤100 coins as possible, and so on down.

# For instance, if you want to give someone ¤468, 
# you would give them four ¤100 coins, 
# two ¤25 coins, one ¤10 coin, one ¤5 coin, and three ¤1 coins, for a total of 11 coins.

#Write a function to return the number of coins you use to make a given amount of change

denoms = [500,100,25,10,5,1]

def change(money):
    # change making function
    if type(money) != int:
        #if money is not an integer, reject 
        print('Please enter integer values only!')
        return

    wallet = {500:0,100:0,25:0,5:0,1:0} #initiate dictonary of values

    for c in denoms:
        wallet[c] = int(money/c)
        money = money - c*wallet[c]
 
    print('The given change is: ', wallet, 'for a toal of ', sum(wallet.values()), '  coins.')
    
#testing

for z in [0,12,468,123456]:
    change(z)