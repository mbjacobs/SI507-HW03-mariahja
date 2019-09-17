import random

def get_question():
    print("Ask me a question...")
    return input ()

def check_question(question_str):
    if question_str.endswith("?"):
        return True
    else:
        print ("I’m sorry, I can only answer questions.")
        return False

if __name__ == "__main__":
    is_valid_question = False
    question = ""

    while question != "quit" or is_valid_question == False:
        question = get_question()
        if check_question(question):
            is_valid_question = True

magic_ball_answers = ["It is certain", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.","Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.","Outlook not so good.", "Very doubtful."]
print(random.choice(magic_ball_answers))