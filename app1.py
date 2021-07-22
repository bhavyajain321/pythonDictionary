import json
from difflib import get_close_matches

data = json.load(open("E:/PYTHON udemy course/application1/data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes or N if no: "% get_close_matches (w, data.keys())[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches (w, data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "The word doesn't exists,please double check it."
        elif yn in data:
            return data[yn]
        else:
            return "We didn't fine your self made word"
    else:
        return "This word doesn't exists.Please double check it."
    

word = input("Enter your word Buddy: ")

output = translate(word)
if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)