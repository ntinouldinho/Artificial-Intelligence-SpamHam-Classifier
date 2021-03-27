from naive_bayes import naive_bayes_run
from naive_bayes import calc_prob
from create_voc_functions import create_vocabulary
from vector_functions import create_vectors
from results import plot_results
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
max_m = 0   
ms = [500,1000,1500]
#vres max sundiasmo uperparametrwn
for m in ms:
        Xs,voc_index,sum_mes,sum_ham_mes = create_vocabulary(m,True,10)
        path_train, vec_emails_train, typ_train = create_vectors(path1,typ1,voc_index)
        path_dev, vec_emails_dev, typ_dev = create_vectors(path2,typ2,voc_index)
        probs = calc_prob(Xs,sum_mes,sum_ham_mes)#dhmiourgia pithanothtwn
        prob_ham = sum_ham_mes/sum_mes
        res1 = naive_bayes_run(vec_emails_dev,typ_dev,probs,prob_ham,voc_index)
        acc = (res1[0][0]+res1[1][1])/(res1[0][0]+res1[0][1]+res1[1][0]+res1[1][1])
        if acc>max_acc:
            max_acc = acc
            max_m = m
print("Max uperparametros m: ",max_m)
   
#apotelesmata sta test dedomena
x=[]
resTests = []
resTrains = []
print("Predict...")
for i in range(10):
        Xs, voc_index,sum_mes,sum_ham_mes = create_vocabulary(max_m,True,i+1)#dhmiourgia vocabulary me vash to kalutero m
        #create vectors
        path_train, vec_emails_train, typ_train = create_vectors(path1,typ1,voc_index)
        path_testm, vec_emails_test, typ_test = create_vectors(path3,typ3,voc_index)
        
        x.append(sum_mes)
        probs = calc_prob(Xs,sum_mes,sum_ham_mes)#dhmiourgia pithanothtwn
        prob_ham = sum_ham_mes/sum_mes
        
        resTest = naive_bayes_run(vec_emails_test,typ_test,probs,prob_ham,voc_index)
        resTrain = naive_bayes_run(vec_emails_train[0:sum_mes],typ_train[0:sum_mes],probs,prob_ham,voc_index)
        resTests.append(resTest)
        resTrains.append(resTrain)
plot_results("test","naive",x,resTests,resTrains)
