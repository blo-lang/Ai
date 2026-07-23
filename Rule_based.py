import re,random #re-analyze user text
from colorama import Fore,init
init(autoreset=True) #initialize colorama
#destination options
destinations = {
  "beach": [
    "Bali", "Maldives", "Phuket", "Zanzibar",
    "Diani Beach", "Boracay", "Seychelles", "Mombasa"
  ],
  "mountain": [
    "Swiss Alps", "Rocky Mountains", "Himalayas",
    "Mount Kenya", "Mount Kilimanjaro",
    "Andes Mountains", "Atlas Mountains", "Mount Elgon"
  ],
  "city": [
    "Tokyo", "Paris", "New York", "London",
    "Dubai", "Singapore", "Cape Town", "Nairobi"
  ],
  "safari": [
    "Maasai Mara", "Serengeti",
    "Amboseli National Park", "Tsavo National Park",
    "Kruger National Park", "Etosha National Park"
  ],
  "island": [
    "Mauritius", "Santorini", "Hawaii",
    "Bora Bora", "Fiji",
    "Galápagos Islands", "Lamu Island"
  ],
  "historical": [
    "Rome", "Athens", "Cairo",
    "Petra", "Machu Picchu",
    "Great Zimbabwe", "Giza Pyramids"
  ],
  "adventure": [
    "Queenstown", "Costa Rica",
    "Patagonia", "Interlaken",
    "Moab", "Whistler"
  ],
  "desert": [
    "Sahara Desert", "Namib Desert",
    "Dubai Desert", "Atacama Desert",
    "Kalahari Desert", "Wadi Rum"
  ]
}
#normalize inputs
def normalize_input(text):
    return re.sub(r"\s+"," ",text.strip().lower())
    #r= Check each and every input
    #\= Removes special characters
    #s= Removes white space
#recommend function
def function():
    print(f"{Fore.CYAN} Weclome to the travelbot")
    print(f"{Fore.MAGENTA} I can recommend the following:")
    print("1.Beach")
    print("2.Mountain")
    print("3.City")
    print("4.Safari")
    print("5.Island")
    print("6.Historical")
    print("7.Adventure")
    print("8.Desert")
    travel_choice=input(f"{Fore.GREEN} Select where you want to travel:")
    cleaned_input=normalize_input(travel_choice)
    if cleaned_input=="beach":
        destination=random.choice(destinations['beach'])
        print(f"{Fore.YELLOW} You can visit the following beach:{destination}")
    if cleaned_input=="mountain":
            destination=random.choice(destinations['mountain'])
            print(f"{Fore.YELLOW} You can visit the following mountain:{destination}")
    if cleaned_input=="city":
            destination=random.choice(destinations['city'])
            print(f"{Fore.YELLOW} You can visit the following city:{destination}")
    if cleaned_input=="safari":
            destination=random.choice(destinations['safari'])
            print(f"{Fore.YELLOW} You can visit the following safari:{destination}")
    if cleaned_input=="island":
            destination=random.choice(destinations['island'])
            print(f"{Fore.YELLOW} You can visit the following island:{destination}")
    if cleaned_input=="historical":
            destination=random.choice(destinations['historical'])
            print(f"{Fore.YELLOW} You can visit the following historical:{destination}")
    if cleaned_input=="adventure":
            destination=random.choice(destinations['adventure'])
            print(f"{Fore.YELLOW} You can visit the following adventure:{destination}")
    if cleaned_input=="desert":
            destination=random.choice(destinations['desert'])
            print(f"{Fore.YELLOW} You can visit the following desert:{destination}")
function()    