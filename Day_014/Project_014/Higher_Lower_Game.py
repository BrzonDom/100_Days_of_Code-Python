from Higher_Lower_Data import data

categories = data[0].keys()

# 0. name
# 1. follower_count
# 2. description
# 3. country

print("Categories:")
for category in categories:
    print(f"  - {category}")
print()

print("People:")
for person in data:

    for category in categories:
        print(f"\t{category}: {person[category]}")
    print()
