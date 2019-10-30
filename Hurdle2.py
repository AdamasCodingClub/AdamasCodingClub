import nltk
def remove_duplcts(noun):
    for i in noun:
        if i not in final:
            final.append(i)
    return final

nouns = []
final = []
g = open("Project_text.txt","r")
line = g.read()
senteces = nltk.sent_tokenize(line)

for i in senteces:
    for word,pos in nltk.pos_tag(nltk.word_tokenize(str(senteces))):
      if pos=='NN' or pos== 'NNP'or pos=='NNPS' or pos=="NNS":
          nouns.append(word)

g.close()

final = remove_duplcts(nouns)

g = open("Project_text1.txt", "w")
g.writelines("%s \n" % item for item in final)


g.close()
g = open("Project_text1.txt", "r")
print(g.read())





