import ast
from bson.json_util import dumps
from flask import request, Response, jsonify, render_template, url_for, redirect
from settings import shared_components
import time

from models.predict_model import get_prediction

def get_initial_response():

    return render_template('index.html')

def get_create_page():

    return render_template('form.html')

def save_predictions():


    db = shared_components['db']
    collection = db.predictions

    try:
        # The time of request
        ts = time.time()
        readable_time = time.ctime(ts)
        
        if request.form:
            # Reading the Form Data
            data = request.form
        elif request.json:
            data = request.json
        else:
            raise TypeError("Invalid Request Format")

        # print(data)

        #Prediction of the sentence acquired from the formdata
        prediction, confidence = get_prediction(data['sentence'])    
        
        record_object = {
            "time_of_request": readable_time,
            "input_sentence": data['sentence'],
            "prediction": prediction,
            'confidence': confidence
        }

        record_data = collection.insert(record_object)

        # print(data_record)

        return render_template('predict.html', pred=prediction, conf=confidence)
    
    except Exception as e:
        # Error while trying to create the resource
        return jsonify({'error':e})

    
def fetch_predictions_records():
    db = shared_components['db']
    collection = db.predictions

    try:
        # Fetch all the record(s)
        records_fetched = collection.find({},{'_id':0})

        # Check if the records are found
        if records_fetched.count() > 0:
            # Prepare the response
            records = dumps(records_fetched)
            resp = Response(records, status=200, mimetype='application/json')
            return resp
        else:
            # No records are found
            return Response("No records are found", status=404)
    except Exception as e:
        print("Exception: {}".format(e))
        # Error while trying to fetch the resource
        return Response("Error while trying to fetch the resource", status=500)


def fetch_predictions_record_emotion(emotion):
    db = shared_components['db']
    collection = db.predictions

    try:
        # Fetch all the record(s)
        records_fetched = collection.find({"prediction":emotion},{'_id':0})

        # Check if the records are found
        if records_fetched.count() > 0:
            # Prepare the response
            records = dumps(records_fetched)
            resp = Response(records, status=200, mimetype='application/json')
            return resp
        else:
            # No records are found
            return Response("No records are found", status=404)
    except Exception as e:
        print("Exception: {}".format(e))
        # Error while trying to fetch the resource
        return Response("Error while trying to fetch the resource", status=500)