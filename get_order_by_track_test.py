import data
import sender_stend_request

#Функция позитивной проверки
def positive_assert_200(track):
    response = sender_stend_request.get_order_by_track(track)
    assert response.status_code == 200

#Функция негативной проверки
def negative_assert_404(track):
    response = sender_stend_request.get_order_by_track(track)
    assert response.status_code == 404
    assert response.json()['message'] == 'Заказ не найден'

#Функция проверки иного параметра
def another_parametr_assert_400(track):
    response = sender_stend_request.get_order_by_track(track)
    assert response.status_code == 400
    assert response.json()['message'] == 'Недостаточно данных для поиска'

#Test1 Запрос с существующим трекером
def test_get_order_success_response():
    positive_assert_200(sender_stend_request.track)

#Test2 Запрос с несуществующим трекером
def test_get_order_error_response():
    negative_assert_404(999999)

#Test3 Запрос без трекера
def test_get_order_with_empty_track_error_response():
    another_parametr_assert_400('')