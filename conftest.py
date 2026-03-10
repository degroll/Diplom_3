import pytest
from selenium import webdriver
import requests
from urls import URL, CREATE_USER, AUTH_ENDPOINT
from data import TEST_ACCOUNT


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = None
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()

    driver.maximize_window()
    
    yield driver

    driver.quit()


@pytest.fixture
def create_user():
    user = TEST_ACCOUNT.copy()
    response = requests.post(f"{URL}{CREATE_USER}", json=TEST_ACCOUNT)
    access_token = response.json().get('accessToken')

    yield user

    headers = {'Authorization': access_token}
    requests.delete(f"{URL}{AUTH_ENDPOINT}", headers=headers)

    