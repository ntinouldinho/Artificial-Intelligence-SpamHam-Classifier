def voc_to_string(voc):
    str=""
    for key, value in voc.items():
        str = str + key + " "
    return str
def listToString(s): 
    str1 = " "
    return (str1.join(s))
def diff(first, second):
        second = set(second)
        return [item for item in first if item not in second]
#epistrefei ta email epksergasmena exontas krathsei mono tis lekseis tou leksikou
def create_array_with_emails(pathemails,typ,voc):
    paths = []
    email = []
    typ2=[]
    for i in range(len(pathemails)):
        f = open(pathemails[i],encoding="utf8")
        try:
            corpus= f.read()
        except:
            i = i + 1
            continue
        bagOfWords = list(corpus.split())
        newbag = diff(bagOfWords,diff(bagOfWords,voc))
        newbagstring=listToString(newbag)
        paths.append(pathemails[i])
        typ2.append(typ[i])
        email.append(newbagstring)
    return paths,email,typ2
#dexere os eisodos emails kai dhmiourgei ta dianismata tous
def create_vectors(pathemail,typ,voc):
    l=len(voc.keys())
    paths,email,typ = create_array_with_emails(pathemail,typ,voc)
    vectors = [0]*len(typ)
    j=0
    for i in email:#gia kathe mail
        vector=[0]*l#dhmiourgise to vector tou
        bagOfWordsA = list(dict.fromkeys(i.split()))#pare tis lekσeis tou email apo mia fora
        for key,value in voc.items():
            if key in bagOfWordsA:#uparxei h leksi
                vector[value]=1
        vectors[j] = vector
        j=j+1
    return paths,vectors,typ
