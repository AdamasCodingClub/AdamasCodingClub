import nltk #natural language text box
#only create a text file function
def create():
    file=open("file.txt","w")
    
    file.write(input())
    
    file.close()
newlist=[] #create a list

#start the program
create() #call the create function
file=open("file.txt","r") #Open the file in right mode
read=file.read() #read the file

r1=nltk.word_tokenize(read) #use word tokenizer to splite words & it is store in list formate
l=len(r1) #length of the list
# check the number of words are above 100 words or not 
if(0<l<100):
    #if less then 100 words then
    print("The paragraph is not accepetebel write some thing or try again")
p1=nltk.pos_tag(r1) #which type of word is it & it is store in tupel list formate
l1=len(p1) #tupel list length
list1=[] #blank list
#for loop to store all the nouns present in paragraph in list1 
for i in range(0,l1):
    temp=p1[i]
    newlist.append(temp[1])
    if(newlist[i]=='NN'):
        list1.append(temp[0])
file.close()
#create newfile in write mode 
newfile=open("file1.txt","w")
l2=len(list1)
for i in range(0,l2):
    newfile.write(list1[i]+' ') # write noune in newfile but each word may have some duplicate word
newfile.close()
#now open new file in read mode
f1=open("file1.txt","r")
read2=f1.read()
r2=nltk.word_tokenize(read2) # break the sentence into a word

final_dic={} # empty dictionary
final=[] # empty list
# if duplicate word is there then don't consider it
for i in r2:
    if(i not in final_dic):
        final_dic[i]=i
for key,value in final_dic.items():
    final.append(value)
f1.close()
#create the final file where only noun are present from starting file 
f2=open("final_file","w") # open the final file in write mode
l4=len(final) # lenght of the list where no duplicate noun or word's are present
for i in range(0,l4):
    f2.write(final[i]+' ') # pest nouns on final text file  
f2.close()
# To print noun's
print("\n\nThe noun's are present in new file is=",l4,"\nAnd the noun's are:\n\n")
f3=open("final_file","r")
txt=f3.read()
print(txt)
f3.close()
