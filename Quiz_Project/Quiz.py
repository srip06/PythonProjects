#Sri Chakri Pamulapati
#Quiz
#CS61002

from glob import glob
import sys
import random

def converting_into_dictionary(quizfile):
    f=open(quizfile,'r')
    words={}
    #to find number of lines in a file
    count=0
    for character in f.read():
        if character == '\n':
            count+=1
    count-=1
    print "Number of words in the given file ",count
    number_of_words=input("Enter number of words for your quiz ")
    if number_of_words < 0 or number_of_words > count:
        print "Number which you had entered is not in range"
        sys.exit(0)

    #Returning to starting postion in the file
    f.seek(0)
    lines=[]
    for l in range(count+1):
        lines.append(f.readline())
    
    #Stroring keys in dictionary

    for k in lines:
        if k != '\n':
            word=k
            i=0
            for c in word:
                if c !=':':
                    i=i+1
                if c == ':':
                    break
            w1=word[0:i]
            w2=word[i+1:-1]
            words[w1]=w2.strip('\n').strip('\r')
    #print "Dictionary"
    #print words
    return words,number_of_words

def dictionary_to_file(newfile,dic):
    f=open(newfile,'w')
    for key in dic:
        string=key+" : "+dic[key]+"\n"
        f.write(string)

def quiz():
    #Extracting and storing all files which are in the same directory
    #print glob("C:/Python27/project_1_AP1/*.txt")
    file_names=[]
    for file in glob("*.txt"):
        file_names.append(file)

    for i in range(len(file_names)):
        print i+1,". ",file_names[i]

    chosen_file=raw_input("Enter file name you need to take quiz ")
    
    ex=chosen_file[-4:]
    if ex == '.txt':
        i=0
    else:
        i=1

    if i==1:
        chosen_file+='.txt'

    exist=0
    for file in file_names:
        if chosen_file == file:
            exist=1
    if exist != 1:
        print "You entered file name does not exits in the directory or you miss speled"
        sys.exit()
                
    quizfile=chosen_file
    print "File you had entered is ",quizfile
    words,number_of_words=converting_into_dictionary(quizfile)
    #print words  
    c=0
    wrong_words={}
    random_keys=random.sample(words.keys(),number_of_words)
    #print random_keys
    for d in random_keys:
        c+=1
        if c == (number_of_words+1):
            break
        print d," : ",
        solution=raw_input("")
        #solution testing
        comma_count=0
        for s in words[d]:
            if s == ',':
                comma_count+=1
        if comma_count == 0:
        
            if words[d]==solution:
                print "correct"
            else:
                print "wrong"
                (k,v)=(d,words[d])
                wrong_words[k]=v
        else:
            testing_word=words[d]
            sol=[]
            index_comma=0
            for j in range(comma_count+1):
                w=""
                for s in testing_word:
                    #print "testing_word ",testing_word
                    if s != ',':
                        index_comma+=1
                        w+=s
                    if s == ',':
                        testing_word=testing_word[index_comma+1:]
                        break;
                sol.append(w)
            #print "sol ",sol
            wrong=0
            for z in range(comma_count+1):
                #print "sol[z]",z,sol[z]
                if sol[z]==solution:
                    print "correct"
                    break
                else:
                    wrong+=1
            if wrong == (comma_count+1):
                print "Wrong"
                (k,v)=(d,words[d])
                wrong_words[k]=v
    store=raw_input("Do you want to store your wrong or missed answers in a file (y/n): ")
    if store == 'y' or store == 'Y':
        newfile=raw_input("Enter a filename ")
        extension=newfile[-4:]
        if extension == '.txt':
            i=0
        else:
            i=1

        if i==1:
            newfile+='.txt'

        f=open(newfile,'w')
        dictionary_to_file(newfile,wrong_words)
        print "File has been created for your refernce."
    else:
        sys.exit(0)

if __name__ == "__main__":
    quiz()
