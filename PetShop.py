# File name: M06 - PA Pet Shop (Redux)
# Short description: This code is meant to calculate the total discount given to the user based off of the items they purchased.
# IST 140 Assignment: M06 - PA Pet Shop (Redux)
# @author Conor Dietz
# @version 1.01 11/18/2025
# date of last revision: N/A
# details of the revision: none

def discount(items, isPet, num_items):
    amount = sum(items)
    num_items = len(items)
    non_pet = 0
    if True in isPet and num_items >= 3:
        for i in range(num_items):
            if not isPet[i]:
                non_pet += items[i]
        discounted_amount = non_pet * .2
        discounted_total = amount - discounted_amount

        prompt = print("Your total with the discount of 20 percent off is $%.2f" % discounted_total)
    else:
        prompt = print("You don't qualify for a discount your total is $%.2f" % amount)
    return prompt

def get_inputs():
    items = []
    isPet = []
    price = float(input("Please enter the price (-1 to exit): "))

    while price != -1:
        items.append(price)
        pet = (input("Is this a pet? (Y or N)(-1 to exit): ")).upper()
        if pet == "Y":
            isPet.append(True)
        else:
            isPet.append(False)
        price = float(input("Please enter the price (-1 to exit): "))
    return items, isPet

def main():
    items, isPet = get_inputs()
    num_items = len(items)
    print(discount(items, isPet, num_items))
    print("This is Conor Dietz's project.")

main()

# This code is meant to ask the user for the prices of all the items they bought until entering sentinal value  of -1.
# After being asked about the price of each item they are asked whether the item is a pet.
# The algorithm then runs to check if the user bought at least one pet and at least 3 items. If this is true it applies the 20% off discount
# and tells the user there total with the 20% already taken off. However, if it is false, it returns that the user doesn't qualify
# for a discount and displays the total price without the 20% off discount.

# Please enter the price: 50
# Is this a pet? (Y or N): n
# Please enter the price: 50
# Is this a pet? (Y or N): n
# Please enter the price: 50
# Is this a pet? (Y or N): y
# Please enter the price: -1
# Your total with the discount of 20 percent off is $130.00

# Please enter the price: 50
# Is this a pet? (Y or N): n
# Please enter the price: 50
# Is this a pet? (Y or N): n
# Please enter the price: 50
# Is this a pet? (Y or N): n
# Please enter the price: -1
# You don't qualify for a discount your total is $150.00