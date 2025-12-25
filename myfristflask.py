from flask import Flask,  flash, redirect, request, render_template, make_response, url_for
import json
import sys 
#import pandas as pd

app = Flask(__name__)


@app.route("/")  #บอกว่าเรียกใช้ web ไหน
def helloworld():
    return "Hello, World!"


if __name__ == "__main__":   # run code 
    app.run(host='localhost',debug=True,port=5001)#host='0.0.0.0' = run on internet ,port=5001




