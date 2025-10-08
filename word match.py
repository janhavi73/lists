def match_words(words):
    ctr=0
    lst=[]

    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr=ctr+1
            lst.append(word)

    print("list of words with first and last chracter same",lst)
    return ctr

count=match_words(['abc','cfc','xyz','aba', '1221'])    
print("number of words with the same first and last character: ",count)
