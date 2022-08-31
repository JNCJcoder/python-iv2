import numpy as np
import matplotlib.pyplot as pl
from sklearn.linear_model import LinearRegression

x = np.array([4, 10, 14, 19, 25, 31]).reshape(-1, 1)
y = np.array([6, 19, 14, 29, 25, 41])

model = LinearRegression().fit(x, y)

y_prev = model.predict(x)
print(y_prev)

r_2 = model.score(x, y)
print(r_2)

pl.scatter(x, y, color="red")
pl.plot(x, y_prev, color="black", linewidth=2)
pl.show()