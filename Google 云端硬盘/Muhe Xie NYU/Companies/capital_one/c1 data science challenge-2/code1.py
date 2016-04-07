import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree, metrics
from sklearn.svm import SVR
from sklearn import tree, metrics
from sklearn.metrics import mean_squared_error

#read data
codetest_train = pd.read_table("codetest_train.txt")
codetest_test = pd.read_table("codetest_test.txt")
X_test = codetest_test

X_train = codetest_train.drop('target',axis =1)
y_train = codetest_train['target']

#replace the null features with column mean in these numeric features (['f_61','f_121','f_215','f_237'] are categorical features)
for i in X_train.columns:
    if i not in ['f_61','f_121','f_215','f_237']:
        X_train[i].replace(np.nan,np.mean(X_train[i]),inplace = True)
        X_test[i].replace(np.nan,np.mean(X_test[i]),inplace = True)

#add dummy variables to replace the 
X_train['f_61_is_a'] =0
X_test['f_61_is_a'] = 0
for i in range(len(X_train)):
    if X_train['f_61'][i] == 'a':
        X_train['f_61_is_a'][i] =1

for i in range(len(X_test)):
    if X_test['f_61'][i] == 'a':
        X_test['f_61_is_a'][i] =1

X_train['f_61_is_b'] =0
X_test['f_61_is_b'] = 0
for i in range(len(X_train)):
    if X_train['f_61'][i] == 'b':
        X_train['f_61_is_b'][i] =1

for i in range(len(X_test)):
    if X_test['f_61'][i] == 'b':
        X_test['f_61_is_b'][i] =1


X_train['f_61_is_c'] =0
X_test['f_61_is_c'] = 0
for i in range(len(X_train)):
    if X_train['f_61'][i] == 'c':
        X_train['f_61_is_c'][i] =1

for i in range(len(X_test)):
    if X_test['f_61'][i] == 'c':
        X_test['f_61_is_c'][i] =1


X_train['f_61_is_d'] =0
X_test['f_61_is_d'] = 0
for i in range(len(X_train)):
    if X_train['f_61'][i] == 'd':
        X_train['f_61_is_d'][i] =1

for i in range(len(X_test)):
    if X_test['f_61'][i] == 'd':
        X_test['f_61_is_d'][i] =1


X_train['f_61_is_e'] =0
X_test['f_61_is_e'] = 0
for i in range(len(X_train)):
    if X_train['f_61'][i] == 'e':
        X_train['f_61_is_e'][i] =1

for i in range(len(X_test)):
    if X_test['f_61'][i] == 'e':
        X_test['f_61_is_e'][i] =1
#after create the dummy, I delete the original column
X_train.drop('f_61',axis=1,inplace=True)
#another way 
X_train['f_121_isA'] = X_train['f_121'] =='A'
X_test['f_121_isA'] = X_test['f_121'] =='A'
X_train['f_121_isB'] = X_train['f_121'] =='B'
X_test['f_121_isB'] = X_test['f_121'] =='B'
X_train['f_121_isC'] = X_train['f_121'] =='C'
X_test['f_121_isC'] = X_test['f_121'] =='C'
X_train['f_121_isD'] = X_train['f_121'] =='D'
X_test['f_121_isD'] = X_test['f_121'] =='D'
X_train['f_121_isE'] = X_train['f_121'] =='E'
X_test['f_121_isE'] = X_test['f_121'] =='E'
X_train['f_121_isF'] = X_train['f_121'] =='F'
X_test['f_121_isF'] = X_test['f_121'] =='F'
