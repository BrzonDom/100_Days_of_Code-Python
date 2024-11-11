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

print("Accounts:")
print()
for account in data:

    str_name = f"Name: {account['name']}"
    str_followers = f"Followers: {account['follower_count']}k"
    str_description = f"Description: {account['description']}"
    str_country = f"Country: {account['country']}"

    print('+' + '-' * max_len + '+')
    print('|' + ' ' * 3 + str_name+ ' ' * (max_len - 3 - len(str_name)) + '|')
    print('+' + '-' * max_len + '+')
    print('|' + ' ' * 7 + str_followers+ ' ' * (max_len - 7 - len(str_followers)) + '|')
    print('|' + ' ' * 7 + str_description+ ' ' * (max_len - 7 - len(str_description)) + '|')
    print('|' + ' ' * 7 + str_country + ' ' * (max_len - 7 - len(str_country)) + '|')
    print('+' + '-' * max_len + '+')
    print()

#
#     max_len = max(max_len, len(str_name), len(str_followers), len(str_description), len(str_country))
#
# print(max_len)

"""

+---+
| A |
+---+
+---------------------------------------------------------------------------------------+
|   Name: NASA                                                                          |
+---------------------------------------------------------------------------------------+
|       Followers: 56k                                                                  |
|       Description: Space agency                                                       |
|       Country: United States                                                          |
+---------------------------------------------------------------------------------------+


+---+
| A |
+---+-----------------------------------------------------------------------------------+
|   Name: NASA                                                                          |
+---------------------------------------------------------------------------------------+
|       Followers: 56k                                                                  |
|       Description: Space agency                                                       |
|       Country: United States                                                          |
+---------------------------------------------------------------------------------------+


+---+-----------------------------------------------------------------------------------+
| A |   Name: NASA                                                                      |
+---------------------------------------------------------------------------------------+
|    Followers: 56k                                                                     |
|    Description: Space agency                                                          |
|    Country: United States                                                             |
+---------------------------------------------------------------------------------------+


+----------+
| Option A |
+----------+----------------------------------------------------------------------------+
|   Name: NASA                                                                          |
+---------------------------------------------------------------------------------------+
|       Followers: 56k                                                                  |
|       Description: Space agency                                                       |
|       Country: United States                                                          |
+---------------------------------------------------------------------------------------+


+----------+----------------------------------------------------------------------------+
|   Name: NASA                                                               | Option A |
+---------------------------------------------------------------------------------------+
|       Followers: 56k                                                                  |
|       Description: Space agency                                                       |
|       Country: United States                                                          |
+---------------------------------------------------------------------------------------+


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
