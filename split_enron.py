#diaxorismos se 3 kathgories:training,development,test
import random
from extra_methods import find_paths_enron
import pickle

filesHam,filesSpam = find_paths_enron("examples\\enron1")#girnaei ola ta monopatia twn arxeiwn
d1 = []
d2 = []
for i in filesHam:
    d1.append(i)
    d2.append('ham')  
for i in filesSpam:
    d1.append(i)
    d2.append('spam')

#RANDOMIZE emails
c = list(zip(d1, d2))
random.shuffle(c)
res = list(zip(*c))

l=len(filesHam+filesSpam)
#write paths for train
path = res[0][0:int(round(l*0.8))]
typ = res[1][0:int(round(l*0.8))]
pickle.dump( path, open( "examples_edit\\training_path.p", "wb" ) )
pickle.dump( typ, open( "examples_edit\\training_types.p", "wb" ) )

#write paths for dev
path = res[0][ int(round(l*0.8)) : int(round(l*0.8))+int(round(l*0.1))]
typ = res[1][ int(round(l*0.8)) : int(round(l*0.8))+int(round(l*0.1))]
pickle.dump( path, open( "examples_edit\\dev_path.p", "wb" ) )
pickle.dump( typ, open( "examples_edit\\dev_types.p", "wb" ) )

#write paths for test
path = res[0][int(round(l*0.8))+int(round(l*0.1)):]
typ = res[1] [int(round(l*0.8))+int(round(l*0.1)):]
pickle.dump( path, open( "examples_edit\\test_path.p", "wb" ) )
pickle.dump( typ, open( "examples_edit\\test_types.p", "wb" ) )





