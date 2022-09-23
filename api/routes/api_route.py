from flask import Flask
from controllers.predict_ctrl import get_initial_response, get_create_page, save_predictions,  fetch_predictions_records, fetch_predictions_record_emotion

def create_route(app):
    """
    Router to route diffrent end points

    """

    app.add_url_rule(rule='/',
                    view_func=get_initial_response, methods=['GET'])
    app.add_url_rule(rule='/api/v1/create',
                    view_func=get_create_page, methods=['GET'])                 
    app.add_url_rule(rule='/api/v1/create',
                    view_func=save_predictions, methods=['POST'])
    app.add_url_rule(rule='/api/v1/predictions/',
                    view_func=fetch_predictions_records, methods=['GET'])
    app.add_url_rule(rule='/api/v1/predictions/<emotion>',
                    view_func=fetch_predictions_record_emotion, methods=['GET'])
    return app