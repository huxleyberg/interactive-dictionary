import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        response = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word,data.keys())[0])
        if response == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif response =="N":
            return "The word doen't exist. Please double check it."
        else:
            return "we didn't understand your entry."
    else:
        return "word does not exist"



word = input("Enter Word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)