from selenium.webdriver.common.by import By


class AuthLocators:
    """Класс содержащий локаторы страницы авторизации."""
    FORM_TITLE = (By.CLASS_NAME, 'card-container__title')  # заголовок веб-формы
    PRODUCT_TITLE = (By.CLASS_NAME, 'what-is__title')  # продуктовый заголовок
    INPUT_TITLE = (By.CLASS_NAME, 'rt-input__placeholder')  # название формы данных
    USERNAME = (By.ID, 'username')  # поле для ввода телефона, почты, логина или лицевого счета
    PASSWORD = (By.ID, 'password')  # поле для ввода пароля
    BTN_LOGIN = (By.ID, 'kc-login')  # кнопка "Войти"
    VK_LINK = (By.ID, 'oidc_vk')  # кнопка авторизации через "VK ID"
    OK_LINK = (By.ID, 'oidc_ok')  # кнопка авторизации через "Одноклассники"
    MAIL_RU_LINK = (By.ID, 'oidc_mail')  # кнопка авторизации через "Мой Мир"
    YA_LINK = (By.ID, 'oidc_ya')  # кнопка авторизации через аккаунт "Яндекс"
    FORGOT_PASSWORD_LINK = (By.ID, 'forgot_password')  # ссылка на восстановление пароля
    REGISTRATION_LINK = (By.ID, 'kc-register')  # ссылка на регистрацию
    LK_NAV_BAR = (By.ID, 'lk-btn')  # кнопка "Личный кабинет"
    ERROR_INVALID_DATA = (By.XPATH, '//*[@id="form-error-message"]')  # сообщение о неверных данных пользователя
    TAB_PHONE = (By.ID, 't-btn-tab-phone')  # таб телефона
    TAB_EMAIL = (By.ID, 't-btn-tab-mail')  # таб почты
    TAB_LOGIN = (By.ID, 't-btn-tab-login')  # таб логина
    TAB_LS = (By.ID, 't-btn-tab-ls')  # таб лицевого счета
    ERROR_MESSAGE = (
        By.CSS_SELECTOR, ".rt-input-container__meta--error")  # сообщение об отсутствии данных пользователя
    AGREEMENT = (By.LINK_TEXT, 'пользовательского соглашения')  # ссылка на пользовательское соглашение
    OFFER_TITLE = (By.CLASS_NAME, 'offer-title')  # заголовок пользовательского соглашения
