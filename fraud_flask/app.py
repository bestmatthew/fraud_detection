from flask import Flask, render_template, request, jsonify
from math import sqrt
import joblib
import json
import numpy as np

app = Flask(__name__)  
loaded_model = joblib.load('tuned_balanced_rf.sav')
high_thresh = 0.48
low_thresh = 0.08

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/model', methods=["GET", "POST"])
def model():
    inputs = request.args
    results = inputs['input_1']
    results = json.loads(results)
    results = np.array(results)
    result = ''
    event_array = results.reshape(1, -1)
    if event_array is not None and event_array is not '': 
        try: 
            pred_prob = loaded_model.predict_proba(event_array)
            prob = pred_prob[:, 1]
            print(prob)
            if prob >= high_thresh: 
                result = 'High Risk'
            elif prob >= low_thresh and prob < high_thresh: 
                result = 'Medium Risk'
            elif prob < low_thresh: 
                result = 'Low Risk'
        except: 
            pass
    print(result)
    return jsonify(model_result=result)

@app.route('/cos_sim', methods=["GET", "POST"])

# no_fraud_event_desc_corpus = 

def cos_sim(event_desc_str):  
  with open('fraud_event_desc_corpus.txt') as json_file:
      data = json.load(json_file)
      print(data)

  
if __name__ == '__main__':
    app.run(debug=True)