import json

data = json.load(open("data.json"))

def translate(w):
    if w in data:
        return data[w]
    else:
        return "The word is not in this dictionary."

word = input("Enter word: ")\

print(translate(word.lower()))
