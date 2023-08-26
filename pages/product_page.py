from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):

	def add_product_to_basket(self):
		self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
		self.solve_quiz_and_get_code()
		
	def should_be_message_that_product_added_to_basket(self):
		assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_ADDED_TO_BASKET), "Message that product is successfully added is not presented"
		product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_HEADER).text
		message_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDED_TO_BASKET).text
		assert product_name == message_product_name, "Product name in the basket should be equal to product name"
	
	def should_be_basket_price_equal_to_product_price(self):
		product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
		basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
		assert product_price == basket_price, "Price in the basket should be the same as the product has"
	
	def solve_quiz_and_get_code(self):
		alert = self.browser.switch_to.alert
		x = alert.text.split(" ")[2]
		answer = str(math.log(abs((12 * math.sin(float(x))))))
		alert.send_keys(answer)
		alert.accept()
		try:
			alert = self.browser.switch_to.alert
			alert_text = alert.text
			print(f"Your code: {alert_text}")
			alert.accept()
		except NoAlertPresentException:
			print("No second alert presented")
		
