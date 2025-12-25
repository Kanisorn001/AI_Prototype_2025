from flask import Flask,  flash, redirect, request, render_template, make_response, url_for
import json
import sys 
#import pandas as pd

app = Flask(__name__)


@app.route("/")  #บอกว่าเรียกใช้ web ไหน
def helloworld():
    return "Hello, World!"

@app.route("/name")
def name():
    return "Kanisorn"

@app.route('/receive_get',methods=['GET']) 
def web_service_API_GET():

    msg = request.args.get('msg')
    name = request.args.get('name')

    print(f'the input message from GET is {msg} from {name}.')

    return f'{msg} from {name} receive!'

@app.route('/request',methods=['POST']) 
def web_service_API_POST():

    payload = request.data.decode("utf-8")
    inmessage = json.loads(payload) # ทำ json

    print(inmessage)
    
    
    json_data = json.dumps({'y': 'received!'}) # ส่งกลับไปว่าได้รับเเล้ววว
    return json_data



if __name__ == "__main__":   # run code 
    app.run(host='localhost',debug=True,port=5001)#host='0.0.0.0' = run on internet ,port=5001




