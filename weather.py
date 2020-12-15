
from flask  import Flask,render_template
from urllib import request

from config import URL,CITY,API_KEY

import json

def getData():
	source= request.urlopen(URL.format(CITY=CITY,API_KEY=API_KEY)).read()
	data  = json.loads(source)
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
