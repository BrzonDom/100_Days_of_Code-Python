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

    str_name = f"Name: {account_current['name']}"
    str_followers = f"Followers: {account_current['follower_count']}k"
    str_description = f"Description: {account_current['description']}"
    str_country = f"Country: {account_current['country']}"

    print("Compare these Accounts:")
    print()

    print("+---------------------------------------------------------------------------------------+")
    print("|   " + str_name + ' ' * (max_len - 3 - len(str_name)) + '|')
    print("+---------------------------------------------------------------------------------------+")
    print("|       " + str_followers + ' ' * (max_len - 7 - len(str_followers)) + '|')
    print("|       " + str_description + ' ' * (max_len - 7 - len(str_description)) + '|')
    print("|       " + str_country + ' ' * (max_len - 7 - len(str_country)) + '|')
    print("+----------------------------------------------------------------------------+----------+")

    str_name = f"Name: {account_next['name']}"
    str_followers = f"Followers: {account_next['follower_count']}k"
    str_description = f"Description: {account_next['description']}"
    str_country = f"Country: {account_next['country']}"

    print("                                        +------+                             | Option B |")
    print("+----------+                            |  VS  |                             +----------+")
    print("| Option A |                            +------+")
    print("+----------+----------------------------------------------------------------------------+")
    print("|   " + str_name + ' ' * (max_len - 3 - len(str_name)) + '|')
    print("+---------------------------------------------------------------------------------------+")
    print("|       " + str_followers + ' ' * (max_len - 7 - len(str_followers)) + '|')
    print("|       " + str_description + ' ' * (max_len - 7 - len(str_description)) + '|')
    print("|       " + str_country + ' ' * (max_len - 7 - len(str_country)) + '|')
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


"""

+---------------------------------------------------------------------------------------+
|   Name: NASA                                                                          |
+---------------------------------------------------------------------------------------+
|       Followers: 56k                                                                  |
|       Description: Space agency                                                       |
|       Country: United States                                                          |
+----------------------------------------------------------------------------+----------+
                                        +------+                             | Option B |
+----------+                            |  VS  |                             +----------+ 
| Option A |                            +------+
+----------+----------------------------------------------------------------------------+
|   Name: NASA                                                                          |
+---------------------------------------------------------------------------------------+
|       Followers: 56k                                                                  |
|       Description: Space agency                                                       |
|       Country: United States                                                          |
+---------------------------------------------------------------------------------------+

"""
