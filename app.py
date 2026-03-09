from flask import Flask, render_template, request
from model import predict_disease

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    fever = int(request.form["fever"])
    cough = int(request.form["cough"])
    breath = int(request.form["breath"])

    result = predict_disease(fever,cough,breath)

    return "Predicted Disease: " + result[0]

if __name__ == "__main__":
    app.run(debug=True)