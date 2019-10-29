# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:18:31 2019

@author: Mohit Kumar Soni
"""
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
file = open("Sample.txt","w")
file.write("A function generator is usually a piece of electronic test equipment or software used to generate different types of electrical waveforms over a wide range of frequencies. Some of the most common waveforms produced by the function generator are the sine wave , square wave, triangular wave and sawtooth shapes. These waveforms can be either repetitive or single-shot which requires an internal or external trigger source. Integrated circuits used to generate waveforms may also be described as function generator ICs.")
file = open("Sample.txt","r")
l=file.read()
file.close()
print('The content of sample file is')
print(l)
w = nltk.word_tokenize(l)
p = nltk.pos_tag(w)
list1,list2=[],[]
for w,p in p:
    if p=='NN' or p=='NNS' or p=='NNP' or p=='NNPS':
        list1.append(w)
for w in list1:
    if w not in list2 :
        list2.append(w)
print('All the nouns in the sample file is as below')
print(list2)

"""
Time Complexity
In this algorithm, 2 loops ar running from 0 to n (i.e. No of words in the sample)
Hence Complexity is
f(n)= n+n+c , c is the constant time foe other operations
therefore
f(n)=O(2n)=O(n)
"""
 
