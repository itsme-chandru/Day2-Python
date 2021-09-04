import sys
import random
import re
f_name=sys.argv[1]    #getting file as input in command line arg
prefix=[]
suffix=[]
palindrome=[]
vowels_split=[]
semicolon_list=[]
with open(f_name) as f:
    f_contents=f.read()
    list_words = f_contents.split()
    capitalize=list_words[:]
    new_list=list_words[:]
    for word in list_words:
        if(word.startswith("To") or word.startswith("to")):                 #prefix
            prefix.append(word)
        if(word.endswith("ing")):                                           #suffix
            suffix.append(word)
        most_repeated_word=max(set(list_words), key=list_words.count)       #most repeated word
        if(word==word[::-1] and len(word)!= 1):                             #palindrome
            palindrome.append(word)
        words_split = re.split("a|e|i|o|u", word)                           #splitting words based on vowels
        vowels_split.append(words_split)
        if(len(word)>=3):
            word1 = word[:2] + word[2].upper() + word[3:]
            capitalize[capitalize.index(word)]=word1                        #capitalize every 3rd letter
        new_list[4]=new_list[4].upper()                                     #convert all the letters in the 5th words to caps



    list_words_new = set(list_words)
    list_words_new = list(list_words_new)                                   #unique words in the file
    myDict=dict(zip(range(len(list_words)), list_words))                    #dict with index as keys and words as values

    f.close()


outputFileName = "output #.txt"
output_num = random.randrange(1, 100)
outputFileName = outputFileName.replace("#", str(output_num))
print(outputFileName)
with open(outputFileName+".txt", mode="w") as op:
        op.write(f"Split the words based on the vowels\n{str(vowels_split)}\n\n")
        op.write(f"Capitalize 3rd letter of every word\n{str(capitalize)}\n\n")
        op.write(f"Capitalize 5th word of the file\n{str(new_list)}\n\n")
        op.write("Content after replacing space with '-' and new line with ';'\n")
        with open(f_name, mode='r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.replace(" ", "-")
                line = line.replace("\n", ";")
                semicolon_list.append(line)
            f.close()
        for words in semicolon_list:
            op.write(words)
        op.close()


print("starting with prefix: ",len(prefix))
print("ending with suffix ",len(suffix))
print("word that repeated maximum times "+"".join(str(most_repeated_word)))
print("palindrome words in the file are "+"".join(str(palindrome)))
print("unique words "+"".join(str(list_words_new)))
print("Dictionary with index and words in the file ",myDict)