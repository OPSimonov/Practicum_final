import configuration
import requests
import data
def post_create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.URL_CREATE_ORDER_PATH,
                         json = body,
                         headers = data.headers);
get_track = post_create_order(data.order_body)
track = get_track.json()
token = track["track"]
def get_track_order():
    return requests.get(configuration.URL_SERVICE + configuration.URL_TRACK_ORDER_PATH + str(token))
response = get_track_order()






