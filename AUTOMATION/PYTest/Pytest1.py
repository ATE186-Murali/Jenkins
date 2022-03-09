import threading
import time

import allure
import pytest
from selenium import webdriver

for x in (1,2):
    print(index(x))

class Testpy():
    @pytest.yield_fixture(scope="function")
    def test_parent(self):
        global a


    def test_chile(self,test_parent):
        print("B")
        a="ABC"
        print(a)



thread1 = threading.Thread(target=Testpy)
thread1.start()
thread2 = threading.Thread(target=Testpy)
thread2.start()



