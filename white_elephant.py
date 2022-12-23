import random

# initialize names to randomize and empty array for randomized names 
names = ["Dakota", "Paxton", "Kaden", "Mackenzie", "Hunter"]
randomize_names = []

# Picks a random name 0-4 
def pick_name():
    rand = random.randint(0,4)
    return names[rand]


# Getting a array of randomized names 
def order_names():
    # while the length of our randomized array is less than five
    # meaning we need to add more names to it not all of them are in the array yet
    count = len(randomize_names)
    while count < 5: 
        # get a random name to work with
        rand_name = pick_name()
        # check if the random name is not already used
        if rand_name not in randomize_names:
            # if its not already in our list of RANDOM NAMES
            # put it in our list
            randomize_names.append(rand_name)
            count += 1
    return randomize_names



def print_random_names(): 
    final_product = order_names()
    order = 1 
    for name in final_product:
        print(order, ": ", name)
        order += 1

print_random_names()