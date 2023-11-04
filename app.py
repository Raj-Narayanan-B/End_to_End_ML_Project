from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from src.mlproject.pipeline.prediction import PredictionPipeline
from src.mlproject.constants import *
from src.mlproject.utils.common import load_yaml

from pathlib import Path #type: ignore
import os
 
application = Flask(__name__)

app = application
@app.route("/", methods = ["GET"])
def homepage():
    return render_template("index.html")

@app.route("/train")
def train():
    os.system("python main.py")
    return "Training is successful!"

@app.route('/predict', methods = ['POST','GET'])
def index():
    schema = load_yaml(Path(SCHEMA_PATH))
    columns = list(schema.COLUMNS)[:-1]
    data_dict = {}
    if request.method=='POST':
        try:
            for i in columns:
                data_dict[i] = float(request.form[i])

            obj = PredictionPipeline()
            predicted_value=obj.prediction(data=data_dict)

            return render_template('results.html',prediction = str(predicted_value))
        
        except Exception as e:
            raise e
    else: 
        return render_template("index.html")

if __name__=="__main__":
    app.run(host="0.0.0.0", port = 8080)
    # app.run(host="0.0.0.0", port = 8080, debug = True)
