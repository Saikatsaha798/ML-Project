from sklearn import linear_model
from sklearn.metrics import mean_absolute_percentage_error
import pandas as pd
import numpy as np

df = pd.read_csv('RELIANCE.csv')
datasets = df.to_numpy()

n = 202        #Enter to Change the TEST DATA

stock_features = datasets[:,3:8]
features_train = stock_features[:-50]
features_test = stock_features[n, np.newaxis]

stock_label = datasets[:,8]
label_train = stock_label[:-50]
label_test = stock_label[n, np.newaxis]

model = linear_model.LinearRegression()
model.fit(features_train, label_train)
predicted = model.predict(features_test)

print("Actual Data : ",label_test[0], "\nData Predicted : ", predicted[0])
print("Error : ",int(mean_absolute_percentage_error(label_test, predicted)*1000)/1000, "%")