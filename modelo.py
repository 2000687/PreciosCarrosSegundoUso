import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder


data = pd.read_csv('cars.csv')


X = data[['Brand','Year','Kilometers_Driven','Fuel_Type','Transmission']]
Y = data['Price']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

clf = DecisionTreeRegressor()
clf.fit(X_train, Y_train)

import pickle

pickle.dump(clf,open('DatasetCarros.pkl','wb'))


"""
manual=1
automatic = 0 

Petrol = 0
Diesel = 1

'Toyota',=1
'Honda','=2
Ford','=3
Maruti','=4
Hyundai','=5
Tata','=6
Mahindra'=7
Volkswagen','=8
Audi','=9
BMW',=10
'Mercedes'=11

"""