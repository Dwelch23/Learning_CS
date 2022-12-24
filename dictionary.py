siblings = {
    "Dakota": 14,
    "Paxton": 16,
    "Kaden": 17,
    "Mackenzie": 19,
    "Hunter": 21
}

# Update dictionay of our sibling 
# Tell age of sibling after 1 year is added to their age
# input is a string
# output is the new age
def birthday(person):
    if person in siblings:
        age = siblings[person]
        siblings[person] = age + 1
        return siblings[person]
    else:
        return "Person is not a sibling"

print(siblings)
choice = input("Choose sibling: ")


print("This will be the age of", choice, ": ", birthday(choice))
print(siblings)
