
import numpy as np
from collections import Counter

class KNN:
    """K Nearest Neighbors algorithm
    Parameters
    ------------
    X : numpy array
        Array should hold all relevant criteria.
        Data should be organized by case x feature
    y : numpy array
        Can be a flat array or with dimensions case x 1.
        Can hold categorical data as strings or integers:
         np.array(['a','b','a','c']) or np.array([0,1,0,2])
    Available methods
    -------------
    predict : function
        Used for the prediction of nearest neighbor"""
    def __init__(self,X,y):
        self.y_dic={}
        self.X=X
        self.m,self.n=X.shape
        self.y=self.categorize(y.reshape(self.m,1))
    def categorize(self,y):
        m,n=y.shape
        new_y=np.zeros((m,1))
        unique_y = np.unique(y)
        for i, item in enumerate(unique_y):
            self.y_dic[i]=item
            new_y[y==item]=i
        return new_y
    def predict(self,case,k):
        """Prediction method
        Parameters
        ------------
        case : numpy array
            An array of features
        k    : integer
            The number of nearest neighbors
            that should be compared.
            For best results use odd numbers
        Returns
        ------------
        return_item : string/int
            Returns case classified based
            on K neighbors"""
        return_item=[]
        X_y_distance=(np.sum((self.X-case)**2,1).reshape(self.m,1))**0.5
        X_y_distance=np.concatenate((X_y_distance,self.y),axis=1)
        X_y_distance=X_y_distance[X_y_distance[:,0].argsort()]
        cnt=Counter(X_y_distance[:k,1])
        for item in cnt.keys():
            if cnt[item]==max(cnt.values()):
                #print(self.y_dic[item])
                return_item.append(self.y_dic[item])
        if len(return_item)>1:
            print('More than one item returned. Please set k to odd')
        else:
            return_item=return_item[0]
        print('Nearest item: {0}'.format(return_item))
        return return_item

