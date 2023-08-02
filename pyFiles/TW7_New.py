import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error

boston =fetch_california_housing()
df_x = pd.DataFrame(boston.data, columns=boston.feature_names)
df_y = pd.DataFrame(boston.target)
print(df_x.describe())
reg = linear_model.LinearRegression()
x_train, x_test, y_train, y_test = train_test_split(
    df_x, df_y, test_size=0.33, random_state=42)
reg.fit(x_train, y_train)
print("\nCOEFFICIENTS", reg.coef_)

y_pred = reg.predict(x_test)
print("\nPREDICTIONS : ", y_pred)

print("\nACTUAL DATA : ", y_test)
print("\nNP MEAN : ", np.mean(y_test - y_pred)**2)
print("\nMEAN SQUARED ERROR :", mean_squared_error(y_test, y_pred))