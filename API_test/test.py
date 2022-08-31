import requests
import json

class JsTestTask():
    def __init__(self, my_response_data):
        self.my_response_data = my_response_data
        self.namelist = []
        self.imagelist = []
        self.pricelist = []
        for item in my_response_data: #преобразовываю "name", "image", "price" в отдельные объекты (разложила по листам)
            self.namelist.append(item['name'])
            self.imagelist.append(item['image'])
            self.pricelist.append(item['price'])

    def text_check_alcatel(self):
        for itemname in self.namelist:
            assert "Alcatel" in itemname

    def text_check_sorted(self):
        assert self.namelist == sorted(self.namelist)


class Tests:
    def test_response(self):
        query_params = {"search": "Alcatel", "sort_field": "name"}
        response=requests.get("https://www.lenvendo.ru/api/js-test-task/", params=query_params)
        assert response.status_code == 200
        #print(response.text)

    def test_check_alcatel_and_sorted(self):
        query_params = {"search": "Alcatel", "sort_field": "name"}
        response = requests.get("https://www.lenvendo.ru/api/js-test-task/", params=query_params)
        all_response_data = json.loads(response.text)
        my_response_data = all_response_data['products']
        text = JsTestTask(my_response_data)
        text.text_check_alcatel()
        text.text_check_sorted()
