#import sys
#import math
from logistic_functions import logistic_reg
from logistic_functions import logistic_run
from create_voc_functions import create_vocabulary
from vector_functions import create_vectors
from results import plot_results
import pickle

epoxes = 5

#for train
path1 = pickle.load( open( "examples_edit\\training_path.p", "rb" ) )
typ1 = pickle.load( open( "examples_edit\\training_types.p", "rb" ) )

#for dev
path2 = pickle.load( open( "examples_edit\\dev_path.p", "rb" ) )
typ2 = pickle.load( open( "examples_edit\\dev_types.p", "rb" ) )

#for test
path3 = pickle.load( open( "examples_edit\\test_path.p", "rb" ) )
typ3 = pickle.load( open( "examples_edit\\test_types.p", "rb" ) )

max_acc = 0
max_eta = 0.01
max_lambda = 0.01
max_m = 500
ms = [500,1000,1500]

#vres max sundiasmo uperparametrwn      
for m in ms:#gia kathe m
        Xs,voc_index = create_vocabulary(m,False,10)
    
        path_train, vec_emails_train, typ_train = create_vectors(path1,typ1,voc_index)
        path_dev, vec_emails_dev, typ_dev = create_vectors(path2,typ2,voc_index)
	
        lamda=0.01
        while(lamda>=0.0001):
                eta=0.01
                while(eta>=0.0001):
                    w = logistic_reg(vec_emails_train, typ_train, eta, epoxes, lamda)#dhmiourgia w
                    res = logistic_run(w,vec_emails_dev,typ_dev)
                    acc=(res[0][0]+res[1][1])/(res[0][0]+res[0][1]+res[1][0]+res[1][1])   
                    if(acc > max_acc):#sundiasmos uperparametrwn me max accuracy
                        max_eta = eta
                        max_lambda = lamda
                        max_m = m
                        max_acc = acc
                    eta=eta*0.1
                lamda=lamda*0.1
print("Max m: ", max_m)
print("Max lambda: ", max_lambda)
print("Max eta: ", max_eta)

#apotelesmata sta test dedomena
Xs, voc_index = create_vocabulary(max_m,False,10)#dhmiourgia vocabulary me vash to kalutero m
path_train, vec_emails_train, typ_train = create_vectors(path1,typ1,voc_index)
path_test, vec_emails_test, typ_test = create_vectors(path3,typ3,voc_index)
x = []
for i in range(10):
    x.append(int(len(vec_emails_train)*(i+1)*10/100))
resTests = []
resTrains = []
print("Predict...")
for i in range(10):
        index = x[i]
        w = logistic_reg(vec_emails_train[0:index],typ_train[0:index],max_eta,epoxes,max_lambda)#dhmiourgia w
        resTest = logistic_run(w,vec_emails_test,typ_test)#test
        resTrain = logistic_run(w,vec_emails_train[0:index],typ_train[0:index])#train
        resTests.append(resTest)
        resTrains.append(resTrain)
plot_results("test", "logistic", x, resTests,resTrains)

