# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 13:29:30 2019

@author: PRAGYAJEET
"""

#Importing Natural Language Tool Kit
import nltk                               

f1 = open("paragraph.txt","w")          #Creating a sample file
f1.write("Humans can expand their knowledge to adapt the changing environment. To do that they must learn. Learning can be simply defined as the acquisition of knowledge or skills through study, experience, or being taught. Although learning is an easy task for most of the people, to acquire new knowledge or skills from data is too hard and complicated for machines. Moreover, the intelligence level of a machine is directly relevant to its learning capability. The study of machine learning tries to deal with this complicated task. In other words, machine learning is the branch of artificial intelligence that tries to find an answer to this question: how to make computer learn? When we say that the machine learns, we mean that the machine is able to make predictions from examples of desired behavior or past observations and information. More formal definition of machine learning by Tom Mitchell is A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E. The definition also indicates the main goal of machine learning: the design of such programs.")
f1 = open("paragraph.txt","r")
lines = f1.read()
f1.close()

print("The paragraph : ")
print(lines)                            #Printing the sample file

words = nltk.word_tokenize(lines)       #Tokenizing the file contents into words
pos_lst = nltk.pos_tag(words)           #List containing words with their POS tag as tuples

temp_lst = []                           
final_lst = []

for word,pos in pos_lst :
    if pos=='NN' or pos=='NNS' or pos=='NNP' or pos=='NNPS' :
        temp_lst.append(word)           #Appending only nouns to a temporary list

for word in temp_lst :
    if word not in final_lst :          #Removing duplicates from the list
        final_lst.append(word)          

f2 = open("final.txt","w")
for word in final_lst :
    f2.write(word)                      #Writing the final list content to final.txt
    f2.write(", ")
    
f2 = open("final.txt","r")
print("Nouns in the paragraph : ")      #Printing file contents of final.txt
print(f2.read())
f2.close()        


"""
Time complexity of the program :
There are three loops in the program, each executing n number of times and rest of the statements run at constant
time.    
That is, Time Complexity = O(3n) = O(n)
"""