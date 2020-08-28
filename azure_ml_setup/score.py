from azureml.core.model import Model
import numpy as np


from keras.models import load_model



def init():
    global model_path
    global classes

    model_path = Model.get_model_path(model_name = 'Predictor')
    model = load_model(model_path)

    classes = []

def run(raw_data):
    try:
        data = np.array(json.loads(raw_data)['data'])
        
        pred = model.predict_classes(data)

        result = classes[pred[0]]
        return {"result": result}
    except Exception as e:
        result = str(e)
        return {"error": result}