import nltk
f1=open("num.txt","w")
f1.write("The lion is a wild animal. It is one of the strongest animals. He is known as the king of the jungle because of its huge size and ferocious appearance. The African lion is the most common type of lion it has the species panther, Leo. The panther also has the common name of a lion and comes from the Felidae family. The lion has a healthy body. It is four-legged, it eats flesh, its paws are powerful. Its footprints are known as pug-marks. It has two sharp eyes; it hunts during the night, lions are the excellent hunter. It sleeps during the daytime.")
f1.close()
f2=open("num.txt","r")
lines=f2.read()
f3=open("num3.txt","w")
print(lines)
words=nltk.word_tokenize(lines)
poss=nltk.pos_tag(words)
print("the parts of speech of each word-")
print(poss)
l1,l2=[],[]
for word,pos in poss:
    if pos=='NN' or pos=='NNP' or pos=='NNPS' or pos=='NNS':
        l1.append(word)
for i in l1:
    if i not in l2:
        l2.append(i)
for i in l2:
    f3.write(i)
    f3.write(",")
f3.close()
f4=open("num3.txt","r")
print("the nouns are-")
print(f4.read())

#in this algorithm number of loops =3
#each loop iterates n times
#time complexity=O(3n)=O(n)
