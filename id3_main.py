from node import Node
from id3 import id3_run
from id3 import id3
from id3 import most_frequent
from results import plot_results
from create_voc_functions import create_vocabulary
from vector_functions import create_vectors
import numpy
import copy
import pickle

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
max_l = 0
max_m = 0   
ms = [500,1000,1500]
#vres max sundiasmo uperparametrwn
for m in ms:
    Xs,voc_index = create_vocabulary(m,False,10)
    
    #create vectors
    path_train, vec_emails_train, typ_train = create_vectors(path1,typ1,voc_index)
    path_dev, vec_emails_dev, typ_dev = create_vectors(path2,typ2,voc_index)

    #stamatame prowra tn epektasi tou dentrou
    par = numpy.arange(0.95, 1.005, 0.01)
    for i in par:
        Xs_tmp = copy.deepcopy(Xs)
        tree = id3(vec_emails_train,typ_train,Xs_tmp,most_frequent(typ_train),i,voc_index)#dhmiourghse to dentro me vash ta px ekpaideusis
        Xs_tmp = copy.deepcopy(Xs)
        res1 = id3_run(tree,vec_emails_dev,typ_dev,voc_index)#des pws ta paei sta development dedomena
        acc = (res1[0][0]+res1[1][1])/(res1[0][0]+res1[0][1]+res1[1][0]+res1[1][1])

        if acc>max_acc:
            max_acc = acc
            max_l = i
            max_m = m
print("Max uperparametros m: ",max_m,"Max uperparametros l: ",max_l)

#apotelesmata sta test dedomena
Xs, voc_index = create_vocabulary(max_m,False,10)#dhmiourgia vocabulary me vash to kalutero m

path_train, vec_emails_train, typ_train = create_vectors(path1,typ1,voc_index)
path_testm, vec_emails_test, typ_test = create_vectors(path3,typ3,voc_index)
x=[]
for i in range(10):
    x.append(int(len(vec_emails_train)*(i+1)*10/100))
resTests = []
resTrains = []
print("Predict...")
for i in range(10):
    Xs_tmp = copy.deepcopy(Xs)
    index = x[i]
    tree = id3(vec_emails_train[0:index],typ_train[0:index],Xs_tmp,most_frequent(typ_train[0:index]),max_l,voc_index)#dhmiourgise dentro me vash to max l
    resTest = id3_run(tree,vec_emails_test,typ_test,voc_index)
    resTrain = id3_run(tree,vec_emails_train[0:index],typ_train[0:index],voc_index)#train
    resTests.append(resTest)
    resTrains.append(resTrain)
plot_results("test", "id3", x, resTests,resTrains)
