import requests as requests
import time
import os
import shutil
import sys
import json
import requests
import cgi
import numpy as np 
from imageio import imread, imwrite 
import cv2
import urllib3
import urllib.request
from PIL import Image
from instabot import Bot
from PIL import Image
from pathlib import Path
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


def do_something(text1):
    word = text1
    token_id = "_ZGXmNxN05csQPqOtJyFRQybjrYJQZ6PaFQD_SIg9so"  
    number = 1
    dimension = 1080  # Unsplash Token ID

    r = requests.get('https://api.unsplash.com/search/collections?query='+word+'&page=1&per_page=30&client_id='+token_id)
    data = r.json()
    data.keys()
    data['total']
    data['total_pages']
    data['results']
    data['results'][0].keys()
    data['results'][0]['cover_photo']
    img_url = ""
    count=0
    for img_data in data['results']:
        file_name = "img/"+ "image"+str(count)+ ".jpg"
        img_url = img_data['cover_photo']['urls']['raw']
        suffix = '&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w='+str(dimension)+'&fit=max'
        print(img_url)
        img_url = img_url + suffix

        count+=1
        if(count>=number):
            break
    print(img_url)
    urllib.request.urlretrieve(img_url,"day.png")
    img = Image.open("day.png")
    arr = img * np.array([0.1,0.2,0.5]) 
    arr2 = (255*arr/arr.max()).astype(np.uint8)
    imwrite('night.png',arr2)
    img2 = cv2.imread('night.png')
    gamma = 1
    gamma_img = np.array(255*(img2/255)
    **gamma,dtype = 'uint8')
    cv2.imwrite('night_final.png',gamma_img)
    print("Conversion done!")
    return "success"



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    word = request.args.get('text1')
    combine = do_something(text1)
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

