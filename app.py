from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("placement_lr.pkl", "rb"))

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        cgpa = float(request.form["cgpa"])
        iq = float(request.form["iq"])
        result = model.predict([[cgpa, iq]])
        return f"Placement: {int(result[0])}"
    return '''
    <form method="post">
        CGPA: <input name="cgpa"><br>
        IQ: <input name="iq"><br>
        <button type="submit">Predict</button>
    </form>
    '''

if __name__ == "__main__":
    app.run()
