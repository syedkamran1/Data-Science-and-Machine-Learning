import pickle,json
import numpy as np
import pandas as pd

__locations = None
__model = None
__cols = None

def load_saved_artifacts():
	print('Loading Artifacts....!')
	global __locations
	global __model
	global __cols
	with open('./artifacts/columns.json','r') as f:
		__cols = json.load(f)['data_columns'] 
		__locations = __cols[3:]
		
		#print(__locations)	

	with open('./artifacts/rental_price_prediction_model.pickle','rb') as f:
		__model = pickle.load(f)

	print("Artifacts Loaded Successfully..")

def predict(location,sqft,bath,bhk):
	x = pd.Index(__cols)
	#print(np.where(x =='sanjay nagar'))
	y = np.zeros(len(x))
	try: 
		y[np.where(x == location)[0][0]]=1
	except:
		return False
	y[0]=bath
	y[1]=bhk
	y[2]=sqft
	return __model.predict([y])

# if __name__ == '__main__':
# 	load_saved_artifacts()
# 	#predict('haralur road',1300.0,2,2)
