
bid ={}
bidding_finished = False
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        big_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} . with the bid of ${highest_bid}")
find_highest_bidder(bidding_record = bid)
while not bidding_finished:
    name = input("wvhat is your name?:")
    price = int(input("what is your price?: $"))
    bid[name]=price
    another = input("is there anyone to bid? type yes or no .")
    if another == "no":
        bidding_finished= True
    
        
    
 
