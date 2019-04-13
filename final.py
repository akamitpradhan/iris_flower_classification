from sklearn.datasets import load_iris
import numpy

from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

#find the name of the flower using different algorithms...
def logistic(final_flower_details,x,y):
    l=LogisticRegression(solver='liblinear',multi_class='auto')
    l.fit(x,y)
    y_pred=l.predict(final_flower_details)
    return y_pred
def k_nearest(final_flower_details,x,y):
    l=KNeighborsClassifier()
    l.fit(x,y)
    y_pred=l.predict(final_flower_details)
    return y_pred
def nav_bayes(final_flower_details,x,y):
    l=GaussianNB()
    l.fit(x,y)
    y_pred=l.predict(final_flower_details)
    return y_pred
def d_tree(final_flower_details,x,y):
    l=DecisionTreeClassifier(criterion = "gini")
    l.fit(x,y)
    y_pred=l.predict(final_flower_details)
    return y_pred

def compute(v,flower_details):
    final_flower_details=[flower_details]
    iris=load_iris()
    x=iris.data
    y=iris.target
    if v==1:
        result=logistic(final_flower_details,x,y)
    elif v==2:
        result=k_nearest(final_flower_details,x,y)
    elif v==3:
        result=nav_bayes(final_flower_details,x,y)
    elif v==4:
        result=d_tree(final_flower_details,x,y)
    return result
