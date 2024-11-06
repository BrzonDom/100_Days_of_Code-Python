# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


name = input("Your Name: ")
price = int(input("Your Bid:  "))
bidders = input("Other bidders (Y/N): ")

auction = {}
auction[name] = price
