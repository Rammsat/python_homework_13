import pytest
import os
from selene.support.shared import browser
from utils.base_session import BaseSession
from dotenv import load_dotenv


load_dotenv()

web_url = os.getenv('WEB_URL')
demoshop_url = BaseSession(web_url)


@pytest.fixture(scope='session')
def demoshop():
    browser.config.base_url = web_url
    browser.config.window_width = 1600
    browser.config.window_height = 1000
    response = demoshop_url.post('/login', json={'Email': 'test_demoshop@gmail.com', 'Password': 'qwe123'},
                                 allow_redirects=False)
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    browser.open("")

    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})

    return browser
