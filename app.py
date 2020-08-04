import pickle
from wsgiref import simple_server
from flask import Flask, request, render_template
from flask import Response
from flask_cors import CORS
import pandas as pd
import numpy as np
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/predict", methods=['POST'])
def predictRoute():
    int_features = [x for x in request.form.values()]
    print(int_features)
    final_features = [np.array(int_features)]
    print(final_features)
    predict = model.predict(final_features)
    print(predict)
    if predict[0] == 3:
        result = 'Wine Quality is Bad'
    elif predict[0] == 4 :
        result = 'Wine Quality is  Below Average'
    elif predict[0]==5:
        result = 'Wine Quality is  Average'
    elif predict[0] == 6:
        result = 'Wine Quality is  Good'
    elif predict[0] == 7:
        result = 'Wine Quality is  Very Good'
    else :
        result = 'Wine Quality is  Excellent'
    return render_template('results.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
    # host = '0.0.0.0'
    # port = 5000