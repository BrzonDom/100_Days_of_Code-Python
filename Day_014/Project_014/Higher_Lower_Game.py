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

print("Compare these Accounts:")
print()
for account in accounts:

    account_print(account)
print()

max_len = 87

# print("Accounts:")
# print()
# for account in data:
#
#     str_name = ' ' * 4 + f"Name: {account['name']}"
#     str_followers = ' ' * 8 + f"Followers: {account['follower_count']}k"
#     str_description = ' ' * 8 + f"Description: {account['description']}"
#     str_country = ' ' * 8 + f"Country: {account['country']}"
#
#     print(str_name)
#     print()
#     print(str_followers)
#     print(str_description)
#     print(str_country)
#     print()
#
#     max_len = max(max_len, len(str_name), len(str_followers), len(str_description), len(str_country))
#
# print(max_len)
