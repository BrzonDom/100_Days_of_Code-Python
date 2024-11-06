# TODO-4: Compare bids in dictionary


name = input("Your Name: ")
price = int(input("Your Bid:  "))
bidders = input("Other bidders (Y/N): ")

auction = {}
auction[name] = price

while bidders == 'Y':
    name = input("Your Name: ")
    price = int(input("Your Bid:  "))
    bidders = input("Other bidders (Y/N): ")

    auction[name] = price
