import sys
import string

def filetodic_art(full_doc_con):
    temp_doc_con = full_doc_con
    #searching for the token and adding the articles into the dictionary
    len_temp_doc = len(temp_doc_con)
    iterate = 0
    len_token = len("<NEW DOCUMENT>")
    art_dic = {}
    count = 0
    while len_temp_doc >= 0:
        # temp_doc_con
        n = temp_doc_con.find("<NEW DOCUMENT>")
        temp_doc_con = temp_doc_con[n+len_token:]
        m = temp_doc_con.find("<NEW DOCUMENT>")
        if m == -1:
            art_dic[count+1] = temp_doc_con.strip('\n')
            break
        art = temp_doc_con[:m]
        art_dic[count+1] = art.strip('\n')
        
        temp_doc_con = temp_doc_con[m:]
        
        len_temp_doc = len(temp_doc_con)
        
        count += 1
    return art_dic


def word_no_art(art_dic):

    word_dic = {}
    word_list = []
    art_dic1 = {}
    for ar in art_dic:
        temp = ""
        for ch in art_dic[ar]:
            if ch != ',':
                temp += ch
        art_dic1[ar] = temp
    # iterating through each article
    for k in art_dic1:
        #taking each article and converting every letter into lower case
        art = art_dic1[k].replace("\n",' ').lower()
        # usin the split function to store all the words in a list
        wl = art.split(' ')
        #  each word is stored into a dictionary as a key and the number of articel as value 
        for l in wl:
            if l in word_dic:
                # if word is already present then we are goin to add the present key i.e the number of article to the set
                word_dic[l].add(k)
            else:
                # sets are used here to store the articles number for each word because sets does not allow duplicates.
                # creating new set with k and the set is stored as value in dictionary
                word_dic[l] = set([k])
        word_list.append(wl)

    return word_dic



def document_retrieval():

    name = raw_input("Enter file name without extension")
    
    num_art = open(name+".txt",'r')

    #storing the file content in one string
    full_doc_con = ""
    for i in num_art:
        if i == "\n":
            pass
        else:   
            full_doc_con += i
        
    #print full_doc_con
    #art_dic stores the number of article and article content as key, value pair
    art_dic = filetodic_art(full_doc_con)
    #print art_dic
    word_dic = word_no_art(art_dic)
    # "words to article numbers"
    # print word_dic

    # displaying options to the user
    while(True):

        print "Select an option bellow"
        print "1. Search for documents"
        print "2. Read Document"
        print "3. Quit Program"
        option = raw_input("=>")

        if option.isdigit():
            option = int(option)

        if option == 1:
            sear_w = raw_input("Enter Search Words: ").lower()
            split_sear_w = sear_w.split(' ')
            c = 0
            total_doc = []
            for w in split_sear_w:
                if w in word_dic:
                    total_doc.append(word_dic[w])
                else:
                    c = 1
            if c == 0:
                #res stores the intersection of words in a given string
                res = total_doc[0]
                # iterating through the artcles set of each word and finding common
                # artcle numberss
                for td in total_doc:
                    res =  res.intersection(td)
                print "Documents fitting search: ",list(res)
            else:
                print "The enetered String is not present in the articles"
                
        elif option == 2:
            doc_num = raw_input("Enter document number: ")
            if doc_num.isdigit():
                doc_num = int(doc_num)
            else:
                print "Entered document number is not correct"

            if doc_num >= 1 and doc_num <= len(art_dic):
                print "The Content in the Article ",doc_num
                print art_dic[doc_num]
            else:
                print "document number is not present in the article"
            
        elif option == 3:
            sys.exit()
            
        else:
            print "Enter correct option (1,2,3)"
        
document_retrieval()




