from utilities.test_data import TestData
from utilities.locators import AuthLocators
from tests.base_test import BaseTest
import pytest


class TestAuth(BaseTest):
    """Класс содержащий тесты аутентификации."""

    def test_form_title_text(self, auth_page):
        """Проверяем название формы авторизации"""
        form_title = auth_page.get_form_title_text()
        assert form_title == "Авторизация"

    @pytest.mark.xfail(reason="Продуктовый слоган не соответствует ТЗ")
    def test_product_title_text(self, auth_page):
        """Проверяем название продуктового слогана"""
        product_title = auth_page.get_product_title()
        assert product_title == "Ростелеком ID"

    @pytest.mark.xfail(reason="Название выбора аутентификации по номеру телефона не соответствует ТЗ")
    def test_authorization_tabs_text(self, auth_page):
        """Проверяем название табов выбора аутентификации"""
        tabs_list = auth_page.get_tabs_list()
        assert tabs_list == ['Номер', 'Почта', 'Логин', 'Лицевой счёт']

    @pytest.mark.xfail(reason="Название формы ввода номера телефона не соответствует ТЗ")
    def test_phone_input_title_text(self, auth_page):
        """Проверяем название формы ввода номера телефона"""
        input_title = auth_page.get_input_title_text()
        assert input_title == "Номер"

    @pytest.mark.xfail(reason="Название формы ввода почты не соответствует ТЗ")
    def test_email_input_title_text(self, auth_page):
        """Проверяем название формы ввода почты"""
        auth_page.click_tab_email()
        input_title = auth_page.get_input_title_text()
        assert input_title == "Почта"

    def test_login_input_title_text(self, auth_page):
        """Проверяем название формы ввода логина"""
        auth_page.click_tab_login()
        input_title = auth_page.get_input_title_text()
        assert input_title == "Логин"

    def test_ls_input_title_text(self, auth_page):
        """Проверяем название формы ввода номера лицевого счета"""
        auth_page.click_tab_ls()
        input_title = auth_page.get_input_title_text()
        assert input_title == "Лицевой счёт"

    @pytest.mark.skip_if_captcha
    @pytest.mark.xfail(reason="Перенаправление клиента на страницу не соответствует ТЗ")
    def test_authorization_relative_link(self, auth_page):
        """Перенаправление на нужную страницу при авторизации с валидными данными"""
        auth_page.log_into_application(TestData.VALID_PHONE, TestData.VALID_PASSWORD)
        relative_link = auth_page.get_relative_link()
        assert "redirect_uri" in relative_link

    @pytest.mark.skip_if_captcha
    def test_valid_phone_authorization(self, auth_page):
        """Авторизация с валидными данными телефона и пароля"""
        auth_page.log_into_application(TestData.VALID_PHONE, TestData.VALID_PASSWORD)
        lk_text = auth_page.get_text(AuthLocators.LK_NAV_BAR)
        assert lk_text == "Личный кабинет"

    @pytest.mark.skip_if_captcha
    def test_valid_email_authorization(self, auth_page):
        """Авторизация с валидными данными почты и пароля"""
        auth_page.click_tab_email()
        auth_page.log_into_application(TestData.VALID_EMAIL, TestData.VALID_PASSWORD)
        lk_text = auth_page.get_text(AuthLocators.LK_NAV_BAR)
        assert lk_text == "Личный кабинет"

    @pytest.mark.skip_if_captcha
    @pytest.mark.parametrize("phone", list(TestData.incorrect_phone.keys()),
                            ids=list(TestData.incorrect_phone.values()))
    def test_invalid_phone_authorization(self, phone, auth_page):
        """Авторизация с некорректными данными телефона"""
        auth_page.log_into_application(phone, TestData.VALID_PASSWORD)
        invalid_text = auth_page.get_invalid_data_text()
        assert invalid_text == "Неверный логин или пароль"

    @pytest.mark.skip_if_captcha
    @pytest.mark.parametrize("email", list(TestData.incorrect_email.keys()),
                            ids=list(TestData.incorrect_email.values()))
    def test_invalid_email_authorization(self, email, auth_page):
        """Авторизация с некорректными данными почты"""
        auth_page.click_tab_email()
        auth_page.log_into_application(email, TestData.VALID_PASSWORD)
        invalid_text = auth_page.get_invalid_data_text()
        assert invalid_text == "Неверный логин или пароль"

    @pytest.mark.skip_if_captcha
    @pytest.mark.parametrize("login", list(TestData.incorrect_login.keys()),
                            ids=list(TestData.incorrect_login.values()))
    def test_invalid_login_authorization(self, login, auth_page):
        """Авторизация с некорректными данными логина"""
        auth_page.click_tab_login()
        auth_page.log_into_application(login, TestData.VALID_PASSWORD)
        invalid_text = auth_page.get_invalid_data_text()
        assert invalid_text == "Неверный логин или пароль"

    @pytest.mark.skip_if_captcha
    @pytest.mark.parametrize("ls", list(TestData.incorrect_ls.keys()),
                            ids=list(TestData.incorrect_ls.values()))
    def test_invalid_ls_authorization(self, ls, auth_page):
        """Авторизация с некорректными данными лицевого счета"""
        auth_page.click_tab_ls()
        auth_page.log_into_application(ls, TestData.VALID_PASSWORD)
        invalid_text = auth_page.get_invalid_data_text()
        assert invalid_text == "Неверный логин или пароль"

    @pytest.mark.skip_if_captcha
    @pytest.mark.parametrize("password", list(TestData.incorrect_password.keys()),
                            ids=list(TestData.incorrect_password.values()))
    def test_invalid_password_authorization(self, password, auth_page):
        """Авторизация с некорректными данными пароля"""
        auth_page.log_into_application(TestData.VALID_PHONE, password)
        invalid_text = auth_page.get_invalid_data_text()
        assert invalid_text == "Неверный логин или пароль"

    def test_authorization_without_email(self, auth_page):
        """Авторизация без данных почты"""
        auth_page.click_tab_email()
        auth_page.set_password(TestData.VALID_PASSWORD)
        auth_page.click_login_button()
        error_text = auth_page.get_error_message_text()
        assert error_text == "Введите адрес, указанный при регистрации"

    def test_authorization_without_phone(self, auth_page):
        """Авторизация без данных телефона"""
        auth_page.set_password(TestData.VALID_PASSWORD)
        auth_page.click_login_button()
        error_text = auth_page.get_error_message_text()
        assert error_text == "Введите номер телефона"

    def test_authorization_without_login(self, auth_page):
        """Авторизация без данных логина"""
        auth_page.click_tab_login()
        auth_page.set_password(TestData.VALID_PASSWORD)
        auth_page.click_login_button()
        error_text = auth_page.get_error_message_text()
        assert error_text == "Введите логин, указанный при регистрации"

    def test_authorization_without_ls(self, auth_page):
        """Авторизация без данных лицевого счета"""
        auth_page.click_tab_ls()
        auth_page.set_password(TestData.VALID_PASSWORD)
        auth_page.click_login_button()
        error_text = auth_page.get_error_message_text()
        assert error_text == "Введите номер вашего лицевого счета"

    def test_vk_authorization_link(self, auth_page):
        """Переход на страницу авторизации с помощью ВК"""
        vk_link = auth_page.get_vk_link()
        assert "https://id.vk.com/auth" in vk_link

    def test_ok_authorization_link(self, auth_page):
        """Переход на страницу авторизации с помощью Одноклассников"""
        ok_link = auth_page.get_ok_link()
        assert "https://connect.ok.ru/dk" in ok_link

    def test_mail_ru_authorization_link(self, auth_page):
        """Переход на страницу авторизации с помощью Маил ру"""
        mail_ru_link = auth_page.get_mail_ru_link()
        assert "https://connect.mail.ru/oauth/authorize" in mail_ru_link

    @pytest.mark.xfail(reason="Перенаправление на страницу авторизации происходит после повторного нажатия")
    def test_ya_authorization_link(self, auth_page):
        """Переход на страницу авторизации с помощью Яндекс"""
        ya_link = auth_page.get_ya_link()
        assert "https://passport.yandex.ru/auth/" in ya_link

    def test_registration_link(self, auth_page):
        """При нажатии на ссылку 'Зарегистрироваться' открывается форма регистрации"""
        auth_page.click_registration_link()
        form_title = auth_page.get_form_title_text()
        assert form_title == "Регистрация"

    def test_forgot_password_link(self, auth_page):
        """При нажатии на ссылку 'Забыл пароль' открывается форма восстановление пароля"""
        auth_page.click_forgot_password_link()
        form_title = auth_page.get_form_title_text()
        assert form_title == "Восстановление пароля"

    def test_agreement_link(self, auth_page):
        """При нажатии на ссылку 'пользовательского соглашения' открывается страница пользовательского соглашения"""
        agreement_title = auth_page.get_agreement_title()
        assert "Публичная оферта о заключении Пользовательского соглашения на использование Сервиса «Ростелеком ID»" \
                == agreement_title
