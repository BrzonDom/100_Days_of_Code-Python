import random
from Higher_Lower_Data import data


def account_print(account, categories):

    print(f"\tName: {account[categories[0]]}")
    print()
    print(f"\t\tFollowers: {account[categories[1]]}k")
    print(f"\t\tDescription: {account[categories[2]]}")
    print(f"\t\tCountry: {account[categories[3]]}")
    print()


categories = tuple(data[0].keys())
# 0. name
# 1. follower_count
# 2. description
# 3. country

print("Categories:")
for category in categories:
    print(f"  - {category}")
print()

account_current = random.choice(data)
account_next = random.choice(data)

while account_next == account_current:
    account_next = random.choice(data)

accounts = [account_current, account_next]

# print(accounts[0])
# print(accounts[1])
# print()

print("Accounts:")
print()
for account in accounts:
    print(f"\tName: {account[categories[0]]}")
    print()
    print(f"\t\tFollowers: {account[categories[1]]}k")
    print(f"\t\tDescription: {account[categories[2]]}")
    print(f"\t\tCountry: {account[categories[3]]}")
    print()
