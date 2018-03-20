from unittest.mock import patch

import pytest
import selenium

from instapy.instapy import InstaPy, InstaPyError


def test_like_by_users_with_no_usernames():
    """test no inputs returns instance without errors"""
    instapy = InstaPy(selenium_local_session=False)
    res = instapy.like_by_users([])
    assert isinstance(res, InstaPy)


@patch('instapy.instapy.webdriver')
def test_set_selenium_local_session_raises_missing_chromedriver(webdriver):
    """Ensure chromedriver is installed"""
    webdriver.Chrome.side_effect = selenium.common.exceptions.WebDriverException()
    with pytest.raises(InstaPyError):
        InstaPy()


@patch('instapy.instapy.webdriver')
def test_set_selenium_local_session_raises_chromedriver_version(webdriver):
    """Ensure chromedriver version is supported"""
    webdriver.Chrome.return_value.capabilities = {'chrome': {
        'chromedriverVersion': '2.35.540470 (e522d04694c7ebea4ba8821272dbef4f9b818c91)'}}
    with pytest.raises(InstaPyError):
        InstaPy()


@patch('instapy.instapy.webdriver')
def test_set_selenium_local_session_supports_chromedriver_version(webdriver):
    """Ensure chromedriver version is supported"""
    webdriver.Chrome.return_value.capabilities = {'chrome': {
        'chromedriverVersion': '2.36.540470 (e522d04694c7ebea4ba8821272dbef4f9b818c91)'}}
    InstaPy()


@patch('instapy.instapy.load_follow_restriction')
def test_set_use_clarifai_raises_on_windows(load_follow_restriction):
    """windows not supported"""
    instapy = InstaPy(selenium_local_session=False)
    with patch('instapy.instapy.os'):
        with pytest.raises(InstaPyError):
            instapy.set_use_clarifai()
