import steamlit #build user interface
#menu
menu = [
    "Pizza", "Burger", "Chicken", "Fries", "Pasta", "Rice", "Sanwich", "Chapati", "Pilau", "Ugali", "Samosa", "Birhyani"
]
#Keypoard layout
keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
positions = {}
for row, keys in enumerate(keyboard):
    for col, letter in enumerate(keys):
        positions[letter] 