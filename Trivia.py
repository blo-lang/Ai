import requests
import html
import random
#function to get the questions
def get_trivia():
    url="https://opentdb.com/api.php?amount=10&category=15&type=multiple"
    try:
        #get the response
        response=requests.get(url,timeout=10)
        #get the status_code
        response.raise_for_status()
        data=response.json()
        if data["response_code"] == 0: #successful
            return data["results"]
        else:
            print("No questions available. Please try again.")
    except requests.RequestException:
        print("Error connection to API url")
        return []
#function-start the quiz
def start_quiz():
    questions=get_trivia()#get the questions
    if not questions:
        return
    score=0
    total=len(questions)#total questions produced
    print("******TRIVIA APP*****")
    print(f"You have {total} questions to answer")
    print("Choose A,B,C or D\n")
    #display the questions and answers
    for number,question in enumerate(questions,start=1):
        #remove the special characters
        question_text=html.unescape(question["question"])
        correct_answer=html.unescape(question["correct_answer"])
        options=[html.unescape(answer) for answer in question["incorrect_answers"]]
        #add all the answers
        options.append(correct_answer)
        random.shuffle(options)
        #display the question
        print(f"\nQuestion {number}:{question_text}")
        #display the answers
        for index,option in enumerate(options):
            print(f"{chr(65+index)}.{option}")
        #get the user input
        while True:
            answer=input("Your answer:").strip().upper()
            if answer in ["A","B","C","D"]:
                break
            print("Invalid CHoice.Enter A,B,C or D")
        selected_answer=options[ord(answer)-ord("A")]
        if selected_answer==correct_answer:
            print("Correct!Well done")
            score+=1
        else:
            print("Incorrect.")
            print(f"The correct answer is :{correct_answer}")
    #print the final results
    print(f"\n=======FINAL RESULTS======")
    print(f"Your score is:{score}/{total}")
    percentage=(score/total)*100
    print(f"pecentage:{percentage:.1f}%")
if __name__=="__main__":
    start_quiz()