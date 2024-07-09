from flask import Flask, jsonify,abort,make_response,request,session,Response
import time
import os
import requests
import sqlite3
import re
from flask_cors import CORS
import json
import random


app =Flask(__name__)
CORS(app)
app.secret_key = "abc"


@app.route("/upload")
def upload():
    list_songs = [["abc", "Undo","abc"],["abc","Fireflies","xy"]]
    return render_template('home.html', username=username,list_of_songs=list_songs,age=dataTransformed)

if __name__=='__main__':
    app.run(debug=True,port=5000,host="0.0.0.0")
