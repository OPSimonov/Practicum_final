#Симонов Олег, 13-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import configuration
import sender_stand_request
import requests
def test_1():
#Выполнить запрос на создание заказа
    def post_create_order(body):
        return requests.post(configuration.URL_SERVICE + configuration.URL_CREATE_ORDER_PATH,
                             json=body,
                             headers=data.headers);
#Сохранить номер трека заказа
    get_track = post_create_order(data.order_body)
    track = get_track.json()
    token = track["track"]
#Выполнить запрос на получение трека заказа
    def get_track_order():
        return requests.get(configuration.URL_SERVICE + configuration.URL_TRACK_ORDER_PATH + str(token))
    response = get_track_order()
#Проверить что код ответа равен 200
    assert response.status_code == 200





