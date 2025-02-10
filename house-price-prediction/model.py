import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.linear_model import LinearRegression

df = pd.read_csv("minihomeprices.csv")

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df["bedrooms"].fillna(df["bedrooms"].median(), inplace=True)
df["bedrooms"] = df["bedrooms"].astype("int64")

sns.pairplot(df, diag_kind='kde')
plt.show()

X = df.drop(["price"], axis=1)
y = df["price"]

mdl = LinearRegression()
mdl.fit(X, y)

y_pred = mdl.predict(X)

print("Intercept: ", mdl.intercept_)
print("Coefficients: ", mdl.coef_)
print("R-squared score: ", mdl.score(X, y))

plt.figure(figsize=(12, 5))
plt.scatter(y, y_pred, color="green", alpha=0.5)
plt.plot([min(y), max(y)], [min(y), max(y)], linestyle="dashed", color="black")
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Prices")

plt.show()



















