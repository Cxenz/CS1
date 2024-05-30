menu_items = ['cauliflower', 'tilapia fillet', 'pork loin', 'green beans',
    'rainbow carrots', 'potatoes', 'three color squash', 'eggplant',
    'eye round of beef', 'baguette'] 
sides = ['with balsamico', 'with garlic and olive oil', 'with minted yogurt',
    'soup', 'chutney', 'salad', 'with salsa', 'over sticky rice', 'au jus',
    'with basmati rice']# parrelel arrays for menu items and sides


num_menu_items = int(input("How many menu items do you need?\n> "))# Get user input for the number of menu items


for i in range(num_menu_items):
    print(menu_items[i % len(menu_items)], sides[i % len(sides)])# Generate the specified number of menu items
