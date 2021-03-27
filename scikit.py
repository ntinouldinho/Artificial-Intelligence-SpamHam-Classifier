from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import Perceptron
from sklearn import tree
from sklearn.metrics import accuracy_score
import pickle
from results import save
from create_voc_functions import create_vocabulary
from vector_functions import create_vectors

#orise m
m = 500

def transformation(typ): #ham,spam->0,1
    res = []
    for i in typ:
        if i == 'ham':
            res.append(0)
        else:
            res.append(1)
    return res
#for train
path1 = pickle.load( open( "examples_edit\\training_path.p", "rb" ) )
typ1 = pickle.load( open( "examples_edit\\training_types.p", "rb" ) )

#for dev
path2 = pickle.load( open( "examples_edit\\dev_path.p", "rb" ) )
typ2 = pickle.load( open( "examples_edit\\dev_types.p", "rb" ) )

#for test
path3 = pickle.load( open( "examples_edit\\test_path.p", "rb" ) )
typ3 = pickle.load( open( "examples_edit\\test_types.p", "rb" ) )

Xs,voc_index = create_vocabulary(m,False,10)

#create vectors
path_train, vec_emails_train, typ_train = create_vectors(path1,typ1,voc_index)
path_test, vec_emails_test, typ_test = create_vectors(path3,typ3,voc_index)

typ_train = transformation(typ_train)
typ_test = transformation(typ_test)

#clf = BernoulliNB()
clf = Perceptron(tol=1e-3, random_state=0)
#clf = tree.DecisionTreeClassifier()

#test
acc1 = []
acc2 = []
x=[]
for i in range(10):
    index = int(len(vec_emails_train)*(i+1)*10/100)
    clf.fit(vec_emails_train[0:index], typ_train[0:index])
    x.append(index)
    #test
    predict1 = clf.predict(vec_emails_test)
    acc_test = accuracy_score(typ_test, predict1)
    acc1.append(acc_test)
    #train
    predict2 = clf.predict(vec_emails_train[0:index])
    acc_train = accuracy_score(typ_train[0:index], predict2)
    acc2.append(acc_train)
    
#save("scikit","naive_bern_acc",x,acc1,acc2,"test")
save("scikit","logistic_acc",x,acc1,acc2,"test")
#save("scikit","dec_tree_acc",x,acc1,acc2,"test")
