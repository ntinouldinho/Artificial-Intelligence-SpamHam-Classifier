import math
import sys
import operator
#entropia
def H(pc0,pc1): 
    if (pc0>0 and pc1>0):
        return (-1)*(pc0*math.log2(pc0)+pc1*math.log2(pc1))
    elif(pc0>0):
        return (-1)*(pc0*math.log2(pc0))
    elif(pc1>0):
        return (-1)*(pc1*math.log2(pc1))
    else:
        return 0 #mhdenikh entropia,ara full vevaiothta
#kerdos pliroforias
def IG(key,word,sum_mes,sum_ham_mes): 
    pexists = word[0]/sum_mes #sunolo twn mhnumatwn pou uparxei h leksi/sunono twn mhnumatwn
    try:
        pham_exists = word[1]/word[0] #sunolo twn ham emfanisewn ths leksis/sunolo twn emfanisewn ths leksis
    except:
        pham_exists = 0
    try:
        pham_notexists = (sum_ham_mes-word[1])/(sum_mes-word[0])#sunolo twn ham mhnumatwn pou uparxei den leksi/sunolo mhnumatwn p den emfanizetai h leksi
    except:
        pham_notexists = 0
    pc0 = H(pham_exists, 1-pham_exists) #pithanothta na exw ham | uparxei h leksi, pithtanothta na exw spam | uparxei h leksi
    pc1 = H(pham_notexists,1-pham_notexists)#pithanothta na exw ham | den uparxei h leksi, pithtanothta na exw  | den uparxei h leksi
    
    return pexists*pc0 + (1-pexists)*pc1
#upologismos kerdous pliroforias gia tis lekseis tou leksikou
def calculate_IGs(voc,sum_mes,sum_ham_mes):
    pc0 = sum_ham_mes/sum_mes #pithanothta na einai ham
    pc1 = (sum_mes-sum_ham_mes)/sum_mes #pithanothta na einai spam
    Hbefore = H(pc0,pc1)
    IGs = dict.fromkeys(voc.keys(), 0)#word->IG
    for key in voc:
        IGs[key] = Hbefore - IG(key,voc[key],sum_mes,sum_ham_mes)
    d = {}
    sorted_IGs = sorted(IGs.items(), key=operator.itemgetter(1),reverse=True)
    return sorted_IGs
