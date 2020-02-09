import pytest
import time


@pytest.mark.usefixtures('setup')
class TestLogin:

    @pytest.mark.parametrize('user, password', [('standard_user', 'secret_sauce'),
                                                ('problem_user', 'secret_sauce'),
                                                ('performance_glitch_user', 'secret_sauce')])
    def test_login_happy_path(self, user, password):
        self.login_page.login(user, password)
        time.sleep(2)
        assert self.login_page.show_burger_btn() is True

    @pytest.mark.parametrize('user, password', [('user', 'password'),
                                                ('locked_out_user', 'secret_sauce')])
    def test_login_invalid_path(self, user, password):
        self.login_page.login(user, password)
        time.sleep(2)
        assert self.login_page.show_error_info() is False
