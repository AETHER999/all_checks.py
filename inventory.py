#!/usr/binenv python3

# Define the initial inventory dictionary with sample data
inventory = {
    'laptop': {'quantity': 10, 'price': 800},
    'printer': {'quantity': 5, 'price': 200},
    'keyboard': {'quantity': 20, 'price': 50},
    'mouse': {'quantity': 15, 'price': 30},
    'monitor': {'quantity': 8, 'price': 400},
    'smartphone': {'quantity': 25, 'price': 200}  # Se cambió 'monitor' por 'smartphone'
}

# Function to display the current inventory
def show_inventory():
    print('\nCurrent inventory:')
    print('--------------------')
    for item, data in inventory.items():
        print(f'{item}: {data["quantity"]} in stock, ${data["price"]} each')

# Function to add a new item to the inventory or increase the quantity of an existing item
def add_item(item, quantity, price):
    if item in inventory:
        inventory[item]['quantity'] += quantity
        inventory[item]['price'] = price
    else:
        inventory[item] = {'quantity': quantity, 'price': price}
    print(f'\nAdded {quantity} {item}(s) to the inventory at ${price} each.')

# Function to remove a certain quantity of an item from the inventory
def remove_item(item, quantity):
    if item in inventory:
        if inventory[item]['quantity'] >= quantity:
            inventory[item]['quantity'] -= quantity
            print(f'\nRemoved {quantity} {item}(s) from the inventory.')
        else:
            print(f'\nNot enough {item}(s) in the inventory.')
    else:
        print(f'\n{item} not found in inventory.')

# Function to calculate the total revenue of the store
def get_revenue():
    revenue = 0
    for item, data in inventory.items():
        revenue += data['quantity'] * data['price']
    return revenue

# Main loop that displays the menu and prompts the user for input
while True:
    print('\nWhat would you like to do?')
    print('1. Show inventory')
    print('2. Add item to inventory')
    print('3. Remove item from inventory')
    print('4. Get total revenue')
    print('5. Quit')
    choice = input('Enter your choice (1-5): ')

    if choice == '1':
        # Show the current inventory
        show_inventory()
    elif choice == '2':
        # Prompt the user for information about the new item and add it to the inventory
        item = input('\nEnter item name: ')
        quantity = int(input('Enter quantity to add: '))
        price = float(input('Enter price per item: '))
        add_item(item, quantity, price)
    elif choice == '3':
        # Prompt the user for information about the item to remove and the quantity to remove
        item = input('\nEnter item name: ')
        quantity = int(input('Enter quantity to remove: '))
        remove_item(item, quantity)
    elif choice == '4':
        # Calculate the total revenue of the store and display it
        revenue = get_revenue()
        print(f'\nTotal revenue: ${revenue:.2f}')
    elif choice == '5':
        # Exit the program
        break
    else:
        # Invalid input, prompt the user to try again
        print('\nInvalid choice. Please enter a number from 1 to 5.')
