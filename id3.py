#id3 algorithm
#create id3 tree
from IG_functions import calculate_IGs
from node import Node
#elegxei an to pososto twn typwn > per(dosmeno pososto)       
def checkType(typ,per):
    h = typ.count('ham')
    if(h/len(typ)>per or h/len(typ)<1-per):
        return True
    else:
        return False
#epistrefei to pio sunithismeno tupo
def most_frequent(List): 
    return max(set(List), key = List.count)#return ham or spam
#epistrefei thn leksi me to max kerdos pliroforias(IG)
def choose_X(email,typ,Xs):
    sum_ham_mes=0
    for word in typ:
        if(word=='ham'):
            sum_ham_mes = sum_ham_mes+1
    
    IGs = calculate_IGs(Xs,len(email),sum_ham_mes)
    return IGs[0]
#epistrefei mail sta opoia uparxei h leksi h opoia vrisketai sto dosmeno index
def find_yes(yes_email,yes_typ,index):
    new_email=[]
    new_typ=[]
    #diatrexw emails
    for i in range(len(yes_typ)):
        #prosthetw afta pou exoun tn leksi
        if (int(yes_email[i][index])>0):
            new_email.append(yes_email[i])
            new_typ.append(yes_typ[i])
    return new_email,new_typ
#epistrefei mail sta opoia den uparxei h leksi h opoia vrisketai sto dosmeno index
def find_no(no_email,no_typ,index):
    new_email=[]
    new_typ=[]
    #diatrexw emails
    for i in range(len(no_email)):
        #prosthetw afta pou den exoun tn leksi
        if (int(no_email[i][index])==0):
            new_email.append(no_email[i])
            new_typ.append(no_typ[i])
    return new_email,new_typ
#ypologismwn twn newn pithanothtwn sta paradeigmata pou proekipsan apo ton diaxorismo
def sums_again(Xs,examples_email,examples_typ,vocabulary):
    newXs={}
    #gia kathe idiothta
    for key in Xs.keys():
        #vres to index ths idiothtas
        index = vocabulary[key]
        sum_ol=0
        sum_ham=0
        for i in range(len(examples_email)):#gia kathe paradeigma
            #des an uparxei h leksi sto paradeigma afto
            if(int(examples_email[i][index])>0):
                sum_ol=sum_ol+1
                if (examples_typ[i]=='ham'):
                    sum_ham = sum_ham + 1
        if(sum_ol>0):
            newXs[key]=[sum_ol,sum_ham]
    return newXs
            
def id3(email,typ,Xs,atrr,per,vocabulary):
    if(len(email)<=0):
        return Node(atrr)
    elif(checkType(typ,per)):
        return Node(most_frequent(typ))
    elif(len(Xs)<=0):
        return Node(most_frequent(typ))
    else:
        X = choose_X(email,typ,Xs)#epilegoume thn idiothta me to max kerdos pliroforias 
        root = Node(X[0])
        m = most_frequent(typ)
        
        del Xs[X[0]]#afairw apo tis idiothtes thn dosmenh
        index = vocabulary[X[0]]#pernw to index ths leksis sto vector
        #emails sta opoia h timh sto index afto einai megalutero tou 0(email[index]>0),dld email sta opoia uparxei h leksi
        examples_yes_email,examples_yes_typ = find_yes(email,typ,index)
        #tropopoihsh twn pithanothtwn t Xs
        Xs1 = sums_again(Xs, examples_yes_email,examples_yes_typ,vocabulary)
        root.right = id3(examples_yes_email,examples_yes_typ,Xs1,m,per,vocabulary)
        
        #emails sta opoia h timh sto index afto einai ish me 0(email[index]=0),dld email sta opoia den uparxei h leksi
        examples_no_email,examples_no_typ = find_no(email,typ,index)
        #tropopoihsh twn pithanothtwn t Xs
        Xs2 = sums_again(Xs,examples_no_email,examples_no_typ,vocabulary)
        root.left = id3(examples_no_email,examples_no_typ,Xs2,m,per,vocabulary)
        
        return root
#trexei ta paradeigmata pou pernei ws eisodo sto dentro 
#epistrefei pinaka me apotelesmata me skopo ton upologismo twn Acc,Pre,Recall,F1
def id3_run(tree,vec_email,typ,vocabulary):
    res = [[0, 0], [0, 0]]
    for i in range(len(typ)):
        ans = tree.find_answer(vec_email[i],vocabulary)
        if (ans=='ham'):
            if(ans == typ[i] ):
                res[0][0] = res[0][0] + 1#truenegative
            else:
                res[1][0] = res[1][0] + 1#falsenegative
        else:
            if(ans == typ[i] ):
                res[1][1] = res[1][1] + 1#truepositive
            else:
                res[0][1] = res[0][1] + 1#falsepositive
    return res

