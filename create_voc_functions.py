#Upologismos IG gia euresh idiothtwn X1,X2,..Xn
from sklearn.feature_extraction.text import CountVectorizer
from IG_functions import H
from IG_functions import IG
from IG_functions import calculate_IGs
import math
import operator
import sys
import pickle

#aukise ton arithmo emfanisis twn leksewn tou leksilogiou me tis lekseis tou email pou dinetai
def add_to_voc(fname,voc,typ):
    f = open(fname,encoding="utf8")
    try:
        corpus= f.read()
    except:
        return 0
    bagOfWordsA = list(dict.fromkeys(corpus.split()))
    for key in bagOfWordsA:
        if key in voc:
            voc[key][0]+=1
        else:
            voc[key]= [1,0]
        if typ=="ham":
            voc[key][1]+=1
    return voc
#dhmiourgei ena dict me kleidi tis lekseis tou leksi kai times:plithos emfanishs leksis,plithos emfanisis leksis se ham mhnumata
#episis epestrepse to sunolo twn mhnumatwn,to sunolo twn ham mhnumatwn
def create_voc(emailpath,typ):
    sum_mes = 0
    sum_ham_mes = 0
    voc = {}
    i = 0
    while i < len(typ):
        res=add_to_voc(emailpath[i],voc,typ[i])
        if res!=0:
            sum_mes+=1
            if typ[i]=="ham":
                sum_ham_mes+=1
            voc=res
        i = i+1
    return voc,sum_mes,sum_ham_mes
#epelekse apo twn pinaka tis protes m lekseis,dld aftes me t megalutero kerdos pliroforias(IG)
def choose_Xs(voc,IGs,m):
    i=-1
    ready_voc={}
    while(i<m-1):
        i+=1
        key = IGs[i][0]
        ready_voc[key]=[voc[key][0],voc[key][1]]
    return ready_voc

#orismata: to plithos twn idiothtwn, an thes na s epistrafoun ta sum h oxi,me poso tis ekato twn paradeigmatwn thes na dhmiourgithei to leksiko
def create_vocabulary(m,wantSums,i):
    path = pickle.load( open( "examples_edit\\training_path.p", "rb" ) )
    typ = pickle.load( open( "examples_edit\\training_types.p", "rb" ) )
    voc,sum_mes,sum_ham_mes = create_voc(path[0:int(len(path)*i*10/100)],typ[0:int(len(path)*i*10/100)])
    IGs = calculate_IGs(voc,sum_mes,sum_ham_mes)
    ready_voc = choose_Xs(voc,IGs,m)#Xs->[sunolo,sunolo se ham]

    voc_index={}
    i=0
    for key in ready_voc.keys():
        voc_index[key] = i
        i = i+1
    if(wantSums==True):
        return ready_voc,voc_index,sum_mes,sum_ham_mes
    else:  
        return ready_voc,voc_index
