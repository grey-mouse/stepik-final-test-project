from selenium.webdriver.common.by import By

class MainPageLocators:
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	
class LoginPageLocators:
	LOGIN_FORM = (By.ID, "login_form")
	LOGIN_EMAIL_FIELD = (By.ID, "id_login-username")
	LOGIN_PASSWORD_FIELD = (By.ID, "id_login-password")
	FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(@href, 'password-reset')]")
	LOGIN_BUTTON = (By.NAME, "login_submit")
	REGISTRATION_FORM = (By.ID, "register_form")
	REGISTER_EMAIL_FIELD = (By.ID, "id_registration-email")
	REGISTER_PASSWORD_FIELD = (By.ID, "id_registration-password1")
	REGISTER_PASSWORD_CONFIRM_FIELD = (By.ID, "id_registration-password2")
	REGISTER_BUTTON = (By.NAME, "registration_submit")
	
class ProductPageLocators:
	ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
	PRODUCT_NAME_HEADER = (By.CSS_SELECTOR, ".product_main > h1")
	MESSAGE_PRODUCT_ADDED_TO_BASKET = (By.CSS_SELECTOR, "#messages > .alert-success:nth-child(1)")
	PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
	BASKET_PRICE = (By.CSS_SELECTOR, "#messages > .alert-info p > strong")
