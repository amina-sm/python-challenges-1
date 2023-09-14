#a counting vowel 
def fun(word):
    lis=[]
    vow=['a','e','i','o','u']
    for c in word:
        for v in vow:
                    if c==v:
                            if  c not in lis:
                                lis.append(c)
    print("Total unique vowels: ",len(lis))
    return lis
name="amina" 
print(fun(name))
                    
