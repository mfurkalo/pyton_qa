import pytest
from modules.ui.page_objects.sign_in_page import SignInPage


@pytest.mark.ui
def test_check_incorrect_username_page_object():

    signInPage = SignInPage()
    signInPage.go_to()
    signInPage.try_login("page_object@gmail.com", "wrong password")
    assert signInPage.chesk_title("Sign in to GitHub · GitHub")
    signInPage.close()
