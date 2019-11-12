"""
封装unittest相关实现
"""
import json
import unittest
import requests
from parameterized import parameterized

import app
from api.loginAPI import Login


def read_json_file():
    data = []
    with open(app.PRO_PATH + "/data/login_data.json", encoding="utf_8")as f:
        for v in json.load(f).values():
            mobile = v.get("mobile")
            password = v.get("password")
            success = v.get("success")
            code = v.get("code")
            message = v.get("message")
            ele = (mobile, password, success, code, message)
            data.append(ele)
    return data


class Test_Login(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.Session()
        self.login_obj = Login()

    def tearDown(self) -> None:
        self.session.close()

    @parameterized.expand(read_json_file())
    def test_login(self, mobile, password, success, code, message):
        print("-" * 100)
        print("参数化读取的数据:", mobile, password, success, code, message)
        response = self.login_obj.login(self.session, mobile, password)
        print("登录响应的结果:", response.json())
        self.assertEqual(success, response.json().get("success"))
        self.assertEqual(code, response.json().get("code"))
        self.assertIn(message, response.json().get("message"))

    def test_login_success(self):
        response = self.login_obj.login(self.session, "13800000002", "123456")
        print("登录成功的结果", response.json())
        # 登录成功的结果 {'success': True, 'code': 10000, 'message': '操作成功！', 'data': '7b3a2252-c859-41b5-83ba-396a99d20ba3'}
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))
        token = response.json().get("data")
        app.TOKEN = token