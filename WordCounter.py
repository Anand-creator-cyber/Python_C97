inputstring = input("Enter text")
print(inputstring)

wordcount = 1
charactercount = 0
for i in inputstring :
    charactercount = charactercount +1
    if(i == " ") :
        wordcount = wordcount+1
print(wordcount)
print(charactercount)
    

    