import requests
#program
while True:
    input("Press Enter to generate joke...")
    api_url="https://official-joke-api.appspot.com/random_joke"
    #get a response
    response=requests.get(api_url)
    #check if response is successfull
    if response.status_code==200:
        #get the joke data
        joke=response.json()
        print("\n" + joke["setup"])
        print(joke["punchline"])
        print()
    else:
        print("Could not fetch a joke. Try again")