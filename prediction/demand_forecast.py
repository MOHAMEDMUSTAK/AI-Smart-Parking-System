import numpy as np
from sklearn.linear_model import LinearRegression

def predict_demand(history):
    if len(history) < 5:
        return np.mean(history) if history else 0

    X = np.arange(len(history)).reshape(-1, 1)
    y = np.array(history)

    model = LinearRegression()
    model.fit(X, y)

    next_hour = np.array([[len(history)]])
    prediction = model.predict(next_hour)

    return max(0, min(1, prediction[0]))
