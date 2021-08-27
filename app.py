
from flask import Flask, render_template
# from flask import Flask
from flask import request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home', methods=['Get', 'Post'])
def index():

    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/' to submit form"
    if request.method == 'POST':
        form_data = request.form.to_dict()
        b = pd.DataFrame(form_data, index=[0])
        filename = 'EE_model_RF.pkl'
        loaded_model = pickle.load(open(filename, 'rb'))
        predict = loaded_model.predict(b)
        Y1 = np.around(predict[:, 0], 2)
        Y2 = np.around(predict[:,1],2)
        f = "The value of Heating load is {y1:}".format(y1=float(Y1))
        g = "The value for Cooling load is {y2}".format(y2=float(Y2))
        return render_template("home.html", prediction1=f, prediction2=g)



if __name__ == '__main__':
    app.run(debug=True)
