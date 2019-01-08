from django.test import TestCase
from .models import User, RoleType
import json


class BaseTest(TestCase):
    def setUp(self):
        self.washer_1 = User.objects.create(id=1, name='washer1', password='test', username='washer1', role=RoleType.WASHER.value)
        self.washer_2 = User.objects.create(id=2, name='washer2', password='test', username='washer2', role=RoleType.WASHER.value)
        self.analyzer_1 = User.objects.create(id=3, name='first_auditor', password='test', username='first', role=RoleType.ANALYZER.value)
        self.analyzer_2 = User.objects.create(id=4, name='second_auditor', password='test', username='second', role=RoleType.ANALYZER.value)

        self.set_user(self.washer_1)

    def set_user(self, user):
        url = '/api/v1/auth/login'
        self.client.post(url, {'username': user.username, 'password': user.password})


class ViewTest(BaseTest):
    def test_user_info(self):
        url = '/api/v1/users/basic/info'
        response = self.client.get(url)
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response.get('id'), 1)

    def test_login_error(self):
        url = '/api/v1/auth/login'
        response = self.client.post(url, {'username': '123', 'password': '222'})
        print(response)

    def test_save_value(self):
        from utils import mongo_client
        from datetime import datetime
        infos = mongo_client.mongo_db.infos
        infos.insert_one({"date": datetime.now()})
        print(infos.find_one().get("_id").generation_time)


