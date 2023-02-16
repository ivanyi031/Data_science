import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
def simple_linear_regression_fit(x_train: np.ndarray, y_train: np.ndarray) -> np.ndarray:
    '''
    Inputs:
    x_train: a (num observations by 1) array holding the values of the predictor variable
    y_train: a (num observations by 1) array holding the values of the response variable

    Returns:
    beta_vals:  a (num_features by 1) array holding the intercept and slope coeficients
    '''
    x_mean=np.mean(x_train)
    y_mean=np.mean(y_train)
    num=np.zeros((x_train.shape[0],))
    den=np.zeros((x_train.shape[0],))
    for i in range(x_train.shape[0]):
        num[i]=(x_train[i]-x_mean)*(y_train[i]-y_mean)
        den[i]=(x_train[i]-x_mean)**2
    beta_1 = sum(num)/sum(den)
    beta_0 = y_mean-beta_1*x_mean
    return np.array([beta_0, beta_1])


def main():
    x_train=np.array([[1],[2],[3]])
    #x_train.reshape((3,1))
    print(x_train.shape)
    y_train=np.array([2,2,4])
    print(y_train.shape)
    plt.scatter(x_train,y_train)
    plt.grid()
    #plt.show()
    
    b=simple_linear_regression_fit(x_train,y_train)
    B0=b[0]
    B1=b[1]
    print(B0,B1)#(B0=1,B1=0.67)
    yfit_data=np.zeros((y_train.shape[0],))
    for i in range(x_train.shape[0]):
        yfit_data[i]=B0+B1*x_train[i]
    print(yfit_data)
    plt.plot(x_train,yfit_data)
    plt.title("simple_linear_regression_fit")
    plt.show()
    reg = LinearRegression().fit(x_train, y_train)
    print(reg.coef_,reg.intercept_)
    sk_yfit=reg.predict(x_train)
    plt.scatter(x_train,y_train)
    plt.grid()
    print(sk_yfit)
    plt.plot(x_train,sk_yfit)
    plt.title("sklearn_linear_regression_fit")
    plt.show()

if __name__ == "__main__":
    main()