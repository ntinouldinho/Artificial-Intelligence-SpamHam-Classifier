#accuracy = (true_positive + true_negative)/total_examples
#prec_positive = true_positives/(true_positives + false_positives)
#recall_positive = true_positives / (true_positives + false_negatives)
#f1_score = 2*((prec*recall)/(prec+recall)
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from extra_methods import write_csv 
def calculate(res):
    try:
        acc = (res[0][0]+res[1][1])/(res[0][0]+res[0][1]+res[1][0]+res[1][1])
    except:
        acc = 0
    try:
        p1 = res[0][0]/(res[0][0]+res[1][0])
    except:
        p1 = 0
    try:
        r1 = res[0][0]/(res[0][0]+res[0][1])
    except:
        r1 = 0
    try:
        p2 = res[1][1]/(res[1][1]+res[0][1])
    except:
        p2 = 0
    try:
        r2 = res[1][1]/(res[1][1]+res[1][0])
    except:
        r2 = 0
    try:
        f1 = (2*(p1*r1))/(p1+r1)
    except:
        f1 = 0
    try:
        f2 = (2*(p2*r2))/(p2+r2)
    except:
        f2 = 0
    return acc,p1,r1,p2,r2,f1,f2
def save(string,name,x,y1,y2,label):
    write_csv(string,name,x,y1,y2)
    plt.title(name)
    plt.xlabel('Number of training examples')
    plt.ylabel(name)
    axes = plt.gca()
    axes.set_ylim([0,1.1])
    line1 = plt.plot(x, y1,label=label)
    line2 = plt.plot(x, y2,label="training")
    plt.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)
    plt.savefig(string+"_res\\"+name+"_"+string+".png")
    plt.close('all')
#x,acc1,acc2,prec_ham1,prec_ham2,recall_ham1,recall_ham2,prec_spam1,prec_spam2,recall_spam1,recall_spam2,f1_score_ham1,f1_score_ham2,f1_score_spam1,f1_score_spam2
def plot_results(label, string, x,resAlt,resTrain):
    acc1 = []
    prec_ham1 = []
    recall_ham1 = []
    prec_spam1 = []
    recall_spam1 = []
    f1_score_ham1 = []
    f1_score_spam1 = []
    acc2 = []
    prec_ham2 = []
    recall_ham2 = []
    prec_spam2 = []
    recall_spam2 = []
    f1_score_ham2 = []
    f1_score_spam2 = []
    for i,j in zip(resAlt,resTrain):
        acc,p1,r1,p2,r2,f1,f2 = calculate(i)
        acc1.append(acc)
        prec_ham1.append(p1)
        recall_ham1.append(r1)
        prec_spam1.append(p2)
        recall_spam1.append(r2)
        f1_score_ham1.append(f1)
        f1_score_spam1.append(f2)
        acc,p1,r1,p2,r2,f1,f2 = calculate(j)
        acc2.append(acc)
        prec_ham2.append(p1)
        recall_ham2.append(r1)
        prec_spam2.append(p2)
        recall_spam2.append(r2)
        f1_score_ham2.append(f1)
        f1_score_spam2.append(f2)
    #Acc
    save(string,"Accuracy",x,acc1,acc2,label)
    
    #Precision Ham
    save(string,'Precision_for_ham',x,prec_ham1,prec_ham2,label)
    
    #Precision Spam
    save(string,'Precision_for_spam',x,prec_spam1,prec_spam2,label)
    
    #Recall Ham
    save(string,'Recall_for_ham',x,recall_ham1,recall_ham2,label)
    
    #Recall Spam
    save(string,'Recall_for_spam',x,recall_spam1,recall_spam2,label)
    
    #F1 score Ham
    save(string,'F1_score_for_ham',x,f1_score_ham1,f1_score_ham2,label)
    
    #F1 score Spam
    save(string,'F1_score_for_spam',x,f1_score_spam1,f1_score_spam2,label)
    
