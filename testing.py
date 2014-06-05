from for_train.train import vec,clf,training_set,target

train  = vec.fit_transform(training_set).toarray()

clf = clf.fit(train,target)

import test

test.test_set = vec.transform(test.extract_features_test).toarray()

print len(test.test_set)