from .pages.main_page import MainPage
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
	#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
	page = ProductPage(browser, link)
	page.open()
	page.add_product_to_basket()
	page.should_be_message_that_product_added_to_basket()
	page.should_be_basket_price_equal_to_product_price()
