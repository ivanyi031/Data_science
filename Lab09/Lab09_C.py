import sklearn
import pandas as pd
import math
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
# load X,Y data
datas = pd.read_csv('epldata_final.csv')
# datas=datas[0:].to_numpy()
# x=[]
# y=[]
# for i in datas:
def get_datas(datas):
    x=[]
    for i in datas[0:].to_numpy():
        fpl_points=i[9]
        age = i[2]
        page_views = i[6]
        new_signing = i[16]
        big_club = i[15]
        position_cat = i[4]
        x.append([fpl_points,age,age**2,math.log2(page_views),new_signing,big_club,position_cat])
    return x
accuracy = []
mse_train = []
mse_test = []
for i in range(100):
    try:
        # Doesn't work: a value is missing
        train_data, test_data = train_test_split(datas, test_size = 0.2, stratify=datas['region'])
    except:
        missing_rows = np.isnan(datas['region'])
        datas = datas.dropna(subset=['region'])
        train_data, test_data = train_test_split(datas, test_size = 0.2, stratify=datas['region'])
    y_train = train_data['market_value']
    y_test = test_data['market_value']
    x_train = get_datas(train_data)
    x_test = get_datas(test_data)
    #print(x_train)
    model = LinearRegression(fit_intercept=True)
    model.fit(x_train,y_train)
    coef = model.coef_
    intercept = model.intercept_
    y_pred = model.predict(x_train)
    mse_train.append(mean_squared_error(y_train,y_pred))
    y_pred_test = model.predict(x_test)
    mse_test.append(mean_squared_error(y_test,y_pred_test)) 
    accuracy.append(model.score(x_test,y_test))

# print(coef)#[ 0.08323629  5.97171287 -0.118532    1.91292639  0.73993252  8.55679854 -0.85683549]
# print(intercept)#-84.64074572375665
plt.plot(np.arange(1,101),mse_train,label='train')
plt.plot(np.arange(1,101),mse_test,color='red',label='test')
plt.legend()
plt.show()
plt.hist(accuracy)
plt.title("accuracy")
plt.show()
#print(accuracy)#0.73