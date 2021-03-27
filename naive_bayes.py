#dexete os eisodo ena email k to katatasei se spam/ham
import math
from id3 import checkType

def calc_prob(Xs,sum_mes,sum_ham_mes):#upologismos pithanothtwn
    new_Xs = {}
    for key in Xs.keys():
        existsHam = (Xs[key][1]+1)/(sum_ham_mes+2)#pithanothta na uparxei dedomenou oti exw ham
        existsSpam = (Xs[key][0]-Xs[key][1]+1)/(sum_mes-sum_ham_mes+2)#pithanothta na uparxei dedomenou oti exw spam
        new_Xs[key] = [existsHam,existsSpam]
    return new_Xs
def naive_bayes(email,Xs,prob_ham,vocabulary):
    p0 = 0#ham
    p1 = 0#spam
    for key in Xs.keys():#gia kathe leksi tou lexikou
        index = vocabulary[key]
        if(email[index]>0):#uparxei h leksi sto mail afto
            p0 = p0 + math.log(Xs[key][0])
            p1 = p1 + math.log(Xs[key][1])
        else:#den uparxei h leksi
            p0 = p0 + math.log(1-Xs[key][0])
            p1 = p1 + math.log(1-Xs[key][1])
    p0 = p0 + math.log(prob_ham)
    p1 = p1 + math.log(1-prob_ham)
    if p0>p1:
        return 'ham'
    else:
        return 'spam'
def naive_bayes_run(vec_email,typ,Xs,prob_ham,vocabulary):
    ans_typ=[]
    res = [[0, 0], [0, 0]]
    for i in range(len(typ)):#gia kathe email
        #vres apantisi naive bayes
        ans = naive_bayes(vec_email[i],Xs,prob_ham,vocabulary)
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
