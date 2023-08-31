from pages.base_page import BasePage
from utilities.locators import AuthLocators


class AuthPage(BasePage):
    """
    Класс представляет страницу авторизации.
    Он наследуется от базовой страницы и содержит специфичные методы и утилиты для страницы авторизации.
    """

    def __init__(self, driver, url=''):
        self.locator = AuthLocators
        if not url:
            url = 'https://b2c.passport.rt.ru'
        super().__init__(driver, url)

    def get_form_title_text(self):
        """Метод получения текста заголовка формы авторизации."""
        title = self.get_text(AuthLocators.FORM_TITLE)
        return title

    def get_product_title(self):
        """Метод получения текста заголовка страницы авторизации."""
        title = self.get_text(self.locator.PRODUCT_TITLE)
        return title

    def click_tab_email(self):
        """Метод клика по вкладке "Почта" на странице авторизации."""
        self.click(self.locator.TAB_EMAIL)

    def click_tab_login(self):
        """Метод клика по вкладке "Логин" на странице авторизации."""
        self.click(self.locator.TAB_LOGIN)

    def click_tab_ls(self):
        """Метод клика по вкладке "Лицевой счет" на странице авторизации."""
        self.click(self.locator.TAB_LS)

    def get_tabs_list(self):
        """Метод получения списка текстов всех вкладок на странице авторизации."""
        lst = [self.get_text(self.locator.TAB_PHONE), self.get_text(self.locator.TAB_EMAIL),
            self.get_text(self.locator.TAB_LOGIN), self.get_text(self.locator.TAB_LS)]
        return lst

    def get_input_title_text(self):
        return self.get_text(self.locator.INPUT_TITLE)

    def set_username(self, username):
        """Метод ввода телефона, почты, логина или лицевого счета в поле для ввода на странице авторизации."""
        self.set(self.locator.USERNAME, username)

    def set_password(self, password):
        """Метод ввода пароля в поле для ввода на странице авторизации."""
        self.set(self.locator.PASSWORD, password)

    def click_login_button(self):
        """Метод клика по кнопке "Войти" на странице авторизации."""
        self.click(self.locator.BTN_LOGIN)

    def click_registration_link(self):
        """Метод клика по ссылке "Регистрация" на странице авторизации."""
        self.click(self.locator.REGISTRATION_LINK)
        self.driver.execute_script("window.stop();")

    def click_forgot_password_link(self):
        """Метод клика по ссылке "Забыл пароль" на странице авторизации."""
        self.click(self.locator.FORGOT_PASSWORD_LINK)
        self.driver.execute_script("window.stop();")

    def log_into_application(self, username, password):
        """Метод авторизации в приложении."""
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()

    def get_invalid_data_text(self):
        """Метод получения текста сообщения об ошибке невалидных данных на странице авторизации."""
        return self.get_text(self.locator.ERROR_INVALID_DATA)

    def get_error_message_text(self):
        """Метод получения текста сообщения об ошибке отсутствия данных на странице авторизации."""
        return self.get_text(self.locator.ERROR_MESSAGE)

    def get_vk_link(self):
        """Метод получения URL ссылки на авторизацию через "VK ID"."""
        self.click(self.locator.VK_LINK)
        link = self.get_link()
        return link

    def get_ok_link(self):
        """Метод получения URL ссылки на авторизацию через "Одноклассники"."""
        self.click(self.locator.OK_LINK)
        link = self.get_link()
        return link

    def get_mail_ru_link(self):
        """Метод получения URL ссылки на авторизацию через "Мой Мир"."""
        self.click(self.locator.MAIL_RU_LINK)
        link = self.get_link()
        return link

    def get_ya_link(self):
        """Метод получения URL ссылки на авторизацию через "Яндекс"."""
        self.click(self.locator.YA_LINK)
        link = self.get_link()
        return link

    def get_agreement_title(self):
        """Метод получения текста заголовка соглашения об использовании со страницы авторизации."""
        self.click(self.locator.AGREEMENT)
        self.switch_window()
        title = self.get_text(self.locator.OFFER_TITLE)
        return title
