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
