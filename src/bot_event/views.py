
def sample_response(input_txt):

    user_msg = str(input_txt).lower()

    if user_msg in ("hello", "hi", "sup",):
        return "Hey! How it is going?"
    
    if user_msg in ("who are you", "who are you?",):
        return "I am bot"
    
    return "I do not understand you"

    
    