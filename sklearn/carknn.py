import sklearn
from sklearn import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import *
import numpy as np
import pandas as pd


data =  pd.read_csv("sklearn/car.data")
#print(data.head())
X = data[[
    "buying",
    "maint",
    "safety"
]].values
y = data[["class"]]

#print(X,y)
#converting X data with LabelEncoder

le = LabelEncoder()

for i in range(len(X[0])):
    X[:,i] = le.fit_transform(X[:,i])

#print(X)

#converting y using mapping

label_mapping = {
    "unacc":0,
    "acc":1,
    "good":2,
    "vgood":3,
}

y["class"] = y["class"].map(label_mapping)
y = np.array(y)
#rint(y)


#create knn model

knn = sklearn.neighbors.KNeighborsClassifier(n_neighbors=25,weights="uniform")

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

knn.fit(X_train,y_train)

prediction = knn.predict(X_test)

accuracy = sklearn.metrics.accuracy_score(y_test,prediction)

print(prediction)
print(accuracy)

print(classification_report(y_test,prediction)) # gives report of precision recall and all scores
a = 1700

print("acctual value:",y[a])
print("predicted val :",knn.predict(X)[a])



knn = sklearn.neighbors.KNeighborsClassifier(n_neighbors=25,weights="uniform")

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

knn.fit(X_train,y_train)

prediction = knn.predict(X_test)

accuracy = sklearn.metrics.accuracy_score(y_test,prediction)
