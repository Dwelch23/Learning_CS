siblings = {
    "Dakota": 14,
    "Paxton": 16,
    "Kaden": 17,
    "Mackenzie": 19,
    "Hunter": 21
}

cur_year = 2022


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

# Adds one to their age for every sibling 
# output updated dictionary
def increment_year():
    for person in siblings:
        birthday(person)
    return siblings


# The function will update the dictionar of the difference of years to all siblings ages
# input is the integer
# output is a updated dictionary
def set_year(year):
    difference = int(year) - cur_year
    num = 0
    while num < difference:
        increment_year()
        num += 1
    return siblings
    

print(siblings)

user_year = input("Choice of year: ")
print(set_year(user_year))