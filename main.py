print("Welcome to my chatbot,Type 'exit' to close the program")
while True: #keeps the program running until the program is closed or stopped
    message=input("You:").lower() #(">>") is the same as ("You:")
    if message=="exit":
        print("Chatbot:Goodbye for now!")
        break #stop the program from running
    elif "hello" in message or "hi" in message or "hey" in message:
        print("Chatbot:Hi there how can i help you today?")
    elif "name" in message:
        print("Chatbot:You have not coded my name yet!")
    elif "gender" in message:
        print("Chatbot:You did not give me a gender!")
    elif "where" in message:
        print("Chatbot:I do not know where")
    elif "why" in message:
        print("Chatbot:I dont know why")
    else:
        print("Chatbot:I do not understand")