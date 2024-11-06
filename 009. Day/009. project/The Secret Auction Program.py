# TODO-4: Compare bids in dictionary


name = input("Your Name: ")
bid = int(input("Your Bid:  "))
bid_more = input("Other bidders (Y/N): ")

auction = {}
auction[name] = bid

while bid_more == 'Y':
    name = input("Your Name: ")
    bid = int(input("Your Bid:  "))
    bid_more = input("Other bidders (Y/N): ")

    auction[name] = bid

max_name = max(auction, key=lambda nm: auction[nm])
max_bid = auction[max_name]
