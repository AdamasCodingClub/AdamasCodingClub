# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 20:51:40 2019

@author: Indranil Dutta
"""


import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
fp=open("FileA.txt","r")#Read the sentence in file A
text=fp.read()
fp.close();
w_t=nltk.word_tokenize(text)
p_t=nltk.pos_tag(w_t)
l1,l2=[],[]
fp=open("FileB.txt","w")
for w,tag in p_t:
    if (tag=='NN' or tag=='NNP' or tag=='NNPS' or tag=='NNS'):
        l1.append(w)
for i in l1:
    if i not in l2:
        l2.append(i)
for i in l2:
    fp.write(i)#Write the nouns in file B
    fp.write("\n")
fp.close()
print(*l2,sep='\n')

#Considering that each of the function calls for NLTK takes O(1) time the time complexity is O(n) for this program