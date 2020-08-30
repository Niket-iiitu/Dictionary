from json import load
from difflib import get_close_matches

def output(text):
    if type(text) == list:
        for _ in text:
            print("\t" + _)
    else:
        print("\t" + text)


data = load(open("data.json"))

print("Welcome to your personal offline digital dictionary.\nType a word on which you want to know. And type '#Bye' to leave.")

while(True):
    word = input("Enter the word: ")
    if word == "#Bye":
        break
    word = word.lower()
    if word in data:
        output(data[word])
    elif word.title() in data:
        output(data[word.title()])
    elif word.upper() in data:
        output(data[word.upper()])
    elif len(get_close_matches(word, data.keys()))>0:
        print("Do you mean: " + get_close_matches(word,data.keys())[0]+" (y/n)?")
        dec = input()
        if dec == 'y' or dec == 'Y':
            output(data[get_close_matches(word, data.keys())[0]])
    else:
        print("\tSorry! I don't understand please try a related word.")
print("Bye, Have a nice day!!!")
