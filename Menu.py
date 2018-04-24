#chicken strips(3.50)/fries(2.50)/burger(4)/hotdog(3.50)/large drink(1.75)/medium drink(1.50)\milkshake(2.25)\salad(3.75)\small drink(1.25)
print('Hello, welcome to my restaurant! the items are listed as follows: 1:Chicken Strips, 2: French Fries, 3: Hamburger, 4: Hotdog, 5: Large Drink, 6: Medium Drink, 7: Milkshake, 8: salad, 9:small drink')

#menu={1:'Chicken Strips', 2: 'French Fries', 3: 'Hamburger', 4: 'Hotdog', 5: 'Large Drink', 6: 'Medium Drink', 7: 'Milkshake', 8: 'salad', 9:'small drink'}

menu_items = [
    [1, "Chicken Strips", 3.75], [2, "French Fries", 2.50],
    [3, "Hamburger", 4.00], [4, "Hot Dog", 3.50], [5, "Large Drink", 1.75],
    [6, "Medium Drink", 1.50], [7, "Milk Shake", 2.25], [8, "Salad", 4.25],
    [9, "Small Drink", 1.25]
]
customer = ""
while customer != 1:
    order= str(input("Please enter each item with the corresponding menu number: "))
    total = 0

    for num in order:
        if num != '0':
            total= total + menu_items[int(num)-1][2] #total
            print("{}           {}".format( menu_items[int(num)-1][1], menu_items[int(num)-1][2]))#print items to receipt
    print ("Your total is $ {}".format(total))
    customer = int(input("type 1 to exit order screen or type 2 to continue with another order \n"))



# I got it to work. Try using save as before running it in powershell to check
