from flask import Flask, request, jsonify
import logging

import util
app = Flask(__name__)


@app.route('/price',methods=['POST'])
def predict_price():

	sqft = float(request.form['sqft'])
	bath = float(request.form['bath'])
	bhk = float(request.form['bhk'])
	location = str(request.form['location'])

	# sqft = float( request.args.get('sqft'))
	# bath = float( request.args.get('bath'))
	# bhk = float( request.args.get('bhk'))
	# location = str( request.args.get('location'))

	logging.warning('sqft = '+ str(sqft) + ' bath = '+ str(bath) + ' bhk = ' + str(bhk) + ' location =  ' + str(location))
	predicted_price = util.predict(location,sqft,bath,bhk)
	if predicted_price != False:
		response = jsonify({
			'predicted_price': predicted_price[0][0]
			})
	else:
		response = jsonify({'status': 'Error :( :('
			})
	return response


@app.route("/",methods=['POST'])
def home():
	return "This is home page"

if __name__ == '__main__':
	print("Starting Python Flask Server....")
	util.load_saved_artifacts()
	app.run()