
name = input("Your Name: ")
bid = int(input("Your Bid:  "))
bid_more = input("Other bidders (Y/N): ")
print()

auction = {}
auction[name] = bid

while bid_more == 'Y':
    name = input("Your Name: ")
    bid = int(input("Your Bid:  "))
    bid_more = input("Other bidders (Y/N): ")
    print()

    auction[name] = bid

max_name = max(auction, key=lambda nm: auction[nm])
max_bid = auction[max_name]

print(f"Winner Name: {max_name}")
print(f"Winner Bid:  {max_bid}")
