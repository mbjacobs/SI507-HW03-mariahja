import random

def get_question():
    print("Ask me a question...")
    return input ()

def check_question(question_str):
    if question_str.endswith("?") or question_str == "quit":
        return True
    else:
        print ("I’m sorry, I can only answer questions.")
        return False

if __name__ == "__main__":
    is_valid_question = False
    question = ""
    magic_ball_answers = ["It is certain", "It is decidedly so.", "Without a doubt.", "Yes - definitely.",
                          "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.",
                          "Signs point to yes.", "Reply hazy, try again.", "Ask again later.",
                          "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
                          "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.",
                          "Very doubtful."]

    #Continue looping while user does not enter "quit"
    while question != "quit":

        #Validate that user has entered a valid question and that question is not quit
        while is_valid_question == False:
            question = get_question()
            is_valid_question = check_question(question)

        if question != "quit":
            print(random.choice(magic_ball_answers))
            is_valid_question = False