import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("dataset.csv")

X = data[["fever","cough","breath_problem"]]
y = data["disease"]

model = DecisionTreeClassifier()
model.fit(X,y)

def predict_disease(fever,cough,breath):
    return model.predict([[fever,cough,breath]])