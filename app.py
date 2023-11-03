from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from src.mlproject.pipeline.prediction import PredictionPipeline
import os

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def homepage():
    return render_template("index.html")

@app.route("/train")
def train():
    os.system("python main.py")
    return "Training is successful!"

if __name__=="__main__":
    app.run(host="0.0.0.0", port = 8080, debug = True)