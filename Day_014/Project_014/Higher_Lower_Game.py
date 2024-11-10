from Higher_Lower_Data import data

categories = tuple(data[0].keys())

# 0. name
# 1. follower_count
# 2. description
# 3. country

print("Categories:")
for category in categories:
    print(f"  - {category}")
print()

print("Accounts:")
print()

for account in data:
    print(f"\tName: {account[categories[0]]}")
    print()
    print(f"\t\tFollowers: {account[categories[1]]}k")
    print(f"\t\tDescription: {account[categories[2]]}")
    print(f"\t\tCountry: {account[categories[3]]}")
    print()
