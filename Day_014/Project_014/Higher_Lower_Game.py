import random
from Higher_Lower_Data import data


def account_print(account):

    print(f"\tName: {account['name']}")
    print()
    print(f"\t\tFollowers: {account['follower_count']}k")
    print(f"\t\tDescription: {account['description']}")
    print(f"\t\tCountry: {account['country']}")
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

print("Accounts:")
print()
for account in accounts:

    account_print(account)

for account in data:

    str_name = f"\tName: {account['name']}"
    str_followers = f"\t\tFollowers: {account['follower_count']}k"
    str_description = f"\t\tDescription: {account['description']}"
    str_country = f"\t\tCountry: {account['country']}"

    print(str_name)
    print()
    print(str_followers)
    print(str_description)
    print(str_country)
    print()
