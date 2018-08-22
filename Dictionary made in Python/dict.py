import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(word):

    if word in data:

        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        tt=input("Did you mean %s instead? Enter Y if Yes ,N if no:" %get_close_matches(word,data.keys())[0])
        if tt=='Y':
            return data[get_close_matches(word,data.keys())[0]]
        elif tt =='N':
            return "Word does not exist.Please double check it"
        else:
            return"we didn't understand your entry"

    else:
        return"The word does not exist.Please recheck it"



inp=input('Enter word :')
inp=inp.lower()
output=(translate(inp))
if type(output)==list:

    for i in output:

        print(i)
else:
    print(output)        
