import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

class Testpy():
    @pytest.yield_fixture(scope="class")
    def test_parent(self):
        print("test parent")
        yield

    @allure.severity(allure.severity_level.CRITICAL)
    def test_first(self,test_parent):
        print("first test")

    @allure.severity(allure.severity_level.NORMAL)
    def test_second(self,test_parent):
       print("second test")