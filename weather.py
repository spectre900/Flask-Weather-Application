from flask  import Flask,render_template

from config import URL,CITY,API_KEY

import json
import requests

def getData(SELECTED_CITY=CITY):
	resp  = requests.get(URL.format(CITY=SELECTED_CITY,API_KEY=API_KEY))
	data  = resp.json()
	data  = {
			'city'       :str(data['name']),
			'longitude'  :str(abs(data['coord']['lon'])) + ('° E ' if (data['coord']['lon']>=0) else '° W '),
			'latitude'   :str(abs(data['coord']['lat'])) + ('° N ' if (data['coord']['lat']>=0) else '° S '),
			'weather'    :str(data['weather'][0]['description']),
			'temperature':str(data['main']['temp']) + '° C ',
			'pressure'   :str(data['main']['pressure']) + ' hPa ',
			'humidity'   :str(data['main']['humidity']) + ' % ',
			'wind'       :str(data['wind']['speed']) + ' m/s ',
	}
	return data

app = Flask(__name__)

@app.route('/')
def home():
        data=getData()
        return render_template('home.html',data=data)