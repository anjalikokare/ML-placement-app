from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("placement_lr.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    status = None

    if request.method == "POST":
        cgpa = float(request.form["cgpa"])
        iq = float(request.form["iq"])

        pred = model.predict([[cgpa, iq]])[0]

        if pred == 1:
            result = "Ho Jayega 😎"
            status = "success"   
        else:
            result = "Thoda Mushkil 😬"
            status = "danger"   

    return render_template("index.html", result=result, status=status)

if __name__ == "__main__":
    app.run()

