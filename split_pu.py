from extra_methods import find_paths_pu
import pickle

train_path = []
train_types =[]
for i in range(8):
    x,y = find_paths_pu("pu_corpora_public\\pu2\\part"+str(i+1))
    for i,j in zip(x,y):
        train_path.append(i)
        train_types.append(j)
dev_paths,dev_types = find_paths_pu("pu_corpora_public\\pu2\\part9")
test_paths,test_types = find_paths_pu("pu_corpora_public\\pu2\\part10")

pickle.dump( train_path, open( "examples_edit\\training_path.p", "wb" ) )
pickle.dump( train_types, open( "examples_edit\\training_types.p", "wb" ) )

pickle.dump( dev_paths, open( "examples_edit\\dev_path.p", "wb" ) )
pickle.dump( dev_types, open( "examples_edit\\dev_types.p", "wb" ) )

pickle.dump( test_paths, open( "examples_edit\\test_path.p", "wb" ) )
pickle.dump( test_types, open( "examples_edit\\test_types.p", "wb" ) )


