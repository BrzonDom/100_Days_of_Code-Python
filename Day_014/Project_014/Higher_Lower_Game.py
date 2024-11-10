from Higher_Lower_Data import data

categories = data[0].keys()

print("Categories:")
for category in categories:
    print(f"  - {category}")
print()

print("People:")
for person in data:
    print(f"\t{person}")
