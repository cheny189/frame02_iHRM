"""
测试员工模块的增删改查实现
"""
import logging
import unittest

import requests

import app
from api.EmpAPI import EmpCRUD


class Test_Emp(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.Session()
        self.emp_obj = EmpCRUD()

    def tearDown(self) -> None:
        self.session.close()

    def test_add(self):
        logging.info("新增员工信息")
        response = self.emp_obj.add(self.session, username="huluwa11111668",
                                    mobile="13012245751")
        print("员工新增响应结果:", response.json())
        id = response.json().get("data").get("id")
        app.USER_ID = id
        # self.assertEqual(True, response.json().get("success"))
        # self.assertEqual(10000, response.json().get("code"))
        # self.assertIn(True, response.json().get("message"))

    def test_update(self, ):
        logging.info("查询员工信息")
        response = self.emp_obj.update(self.session, app.USER_ID, "aotuman11111")
        print("修改后的员工信息", response.json())

    def test_get(self):
        logging.info("获取员工信息")
        response = self.emp_obj.get(self.session, app.USER_ID)
        print("查询到的员工信息", response.json())

    def test_delete(self):
        logging.warning("删除员工信息")
        response = self.emp_obj.delete(self.session, app.USER_ID)
        print("删除到的员工信息", response.json())
