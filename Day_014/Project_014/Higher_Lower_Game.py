import random
from Higher_Lower_Data import data


def account_print(account):

    max_len = 87

    str_name = f"Name: {account['name']}"
    str_followers = f"Followers: {account['follower_count']}k"
    str_description = f"Description: {account['description']}"
    str_country = f"Country: {account['country']}"

    print("+---------------------------------------------------------------------------------------+")
    print("|   " + str_name + ' ' * (max_len - 3 - len(str_name)) + '|')
    print("+---------------------------------------------------------------------------------------+")
    print("|       " + str_followers + ' ' * (max_len - 7 - len(str_followers)) + '|')
    print("|       " + str_description + ' ' * (max_len - 7 - len(str_description)) + '|')
    print("|       " + str_country + ' ' * (max_len - 7 - len(str_country)) + '|')
    print("+---------------------------------------------------------------------------------------+")
    print()


def account_compare_print(accounts):

    account_current, accounts_next = accounts

    max_len = 87

    name_cur = account_current['name']
    followers_cur = account_current['follower_count']
    description_cur = account_current['description']
    country_cur = account_current['country']

    name_nxt = account_next['name']
    followers_nxt = account_next['follower_count']
    description_nxt = account_next['description']
    country_nxt = account_next['country']

    print("Compare these Accounts:")
    print()
    print("+---------------------------------------------------------------------------------------+")
    print("|   Name: " + name_cur + ' ' * (max_len - (3 + 6) - len(name_cur)) + '|')
    print("+---------------------------------------------------------------------------------------+")
    print("|       Followers: " + str(followers_cur) + ' ' * (max_len - (7 + 11) - len(str(followers_cur))) + '|')
    print("|       Description: " + description_cur + ' ' * (max_len - (7 + 13) - len(description_cur)) + '|')
    print("|       Country: " + country_cur + ' ' * (max_len - (7 + 9) - len(country_cur)) + '|')
    print("+----------------------------------------------------------------------------+----------+")
    print("                                        +------+                             | Option B |")
    print("+----------+                            |  VS  |                             +----------+")
    print("| Option A |                            +------+")
    print("+----------+----------------------------------------------------------------------------+")
    print("|   Name: " + name_nxt + ' ' * (max_len - (3 + 6) - len(name_nxt)) + '|')
    print("+---------------------------------------------------------------------------------------+")
    print("|       Followers: " + str(followers_nxt) + ' ' * (max_len - (7 + 11) - len(str(followers_nxt))) + '|')
    print("|       Description: " + description_nxt + ' ' * (max_len - (7 + 13) - len(description_nxt)) + '|')
    print("|       Country: " + country_nxt + ' ' * (max_len - (7 + 9) - len(country_nxt)) + '|')
    print("+---------------------------------------------------------------------------------------+")
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

account_compare_print(accounts)

# max_len = 87
#
# print("Accounts:")
# print()
# for account in data:
#
#     account_print(account)
