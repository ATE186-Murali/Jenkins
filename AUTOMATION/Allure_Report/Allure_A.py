from selenium import webdriver

site_url = 'https://qxf2.com/'


def test_site_title():
    "Checks Qxf2's website title"

    driver = webdriver.Chrome(executable_path="E:\\driver\\chromedriver.exe")
    driver.get(site_url)
    assert driver.title == 'Qxf2 Services: Outsourced Software QA for startups'