import math
import numpy as np
import random
#sigmoidhs
def sigmoid(w,x):
    multi = 0
    for i in range(len(w)):
        if(x[i]>0):
            multi = multi + w[i]
    return 1/(1 + math.exp(-multi))
#stoxastiki anavasi klisis, me oro kanonikopoihshs
def logistic_reg(email,typ,eta,maxStep,lamda):
    wlen = len(email[0])+1
    ws = [random.uniform(-1, 1)for iter in range(wlen)]
    for step in range(maxStep):
        s = 0
        for i in range(len(typ)):#gia ola ta paradeigmata ekpaideusis
            x = list(email[i])
            x.append(1)
            if typ[i]=='ham':
                y=1
                lw = math.log(sigmoid(ws,x))
            else:
                y=0
                lw = math.log(1 - sigmoid(ws,x))
            sum_w=0
            for i in range(len(ws)):
                sum_w = sum_w + ws[i]**2
            s = s + lw - lamda * sum_w
            tmp = y - sigmoid(ws,x)
            for l in range(wlen):#enhmerose ta varh w
                ws[l] = (1-2*lamda*eta)*ws[l] +  eta * tmp * x[l]
        if(s == 0):
            break
    return ws
#trexei ta paradeigmata pou pernei ws eisodo me vash t dosmena w
#epistrefei pinaka me apotelesmata me skopo ton upologismo twn Acc,Pre,Recall,F1
def logistic_run(w,x,typ):
    res = [[0, 0], [0, 0]]
    for i in range(len(typ)):
        xi = list(x[i])
        xi.append(1)
        probplus = sigmoid(w,xi)
        if(probplus>=0.5):
            #theoro oti anhkei sth thetiki kathgoria
            ans='ham'
        else:
            #theoro oti anhkei sthn arnhtikh kathgoria
            ans='spam'
          
        if (ans=='ham'):
            if(ans == typ[i]):
                res[0][0] = res[0][0] + 1#truenegative
            else:
                res[1][0] = res[1][0] + 1#falsenegative
        else:
            if(ans == typ[i] ):
                res[1][1] = res[1][1] + 1#truepositive
            else:
                res[0][1] = res[0][1] + 1#falsepositive
    return res
