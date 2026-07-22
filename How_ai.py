from textblob import TextBlob
import colorama #colored inputs
from colorama import Fore, Style
#initialize colorama
#welcome statement
print(f"{Fore.CYAN}Weclome to the sentiment Analyzer,enter a sentence to detect your mood")
name=input(f"{Fore.YELLOW} Enter your Name:")
#program loop
while True:
    text=input(f"{Fore.GREEN}Enter a Sentence to analyze:")
    #typed exit
    if text.lower()=="exit":
        print(f"{Fore.MAGENTA} Exiting...........")
        break
    if text.lower()=="":
        print(f"{Fore.YELLOW} Please enter an input to analyze")
        continue #restart the loop,ask the user to enter a statement again
    #calculate the polarity(determine your sentiment)
    polarity=TextBlob(text).sentiment.polarity
    #categorize base on polarity
    if polarity>0:
        #happy
        print(f"{Fore.GREEN} Positive sentiment detected")
    elif polarity<0:
        #sad
        print(f"{Fore.RED} Negative sentiment detected")
    else:
        print(f"{Fore.YELLOW} Neutral sentiment detected")
    print(f"Polarity Score is:{polarity:.2f}")