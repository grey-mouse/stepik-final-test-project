import pytest
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])

#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason="bug")),
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser, link):
	#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
	page = ProductPage(browser, link)
	page.open()
	page.add_product_to_basket()
	page.should_be_message_that_product_added_to_basket()
	page.should_be_basket_price_equal_to_product_price()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
@pytest.mark.xfail(reason="bug")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
	page = ProductPage(browser, link)
	page.open()
	page.add_product_to_basket()
	assert page.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_ADDED_TO_BASKET), "Success message should not be presented after adding product to basket"

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_cant_see_success_message(browser, link):
	page = ProductPage(browser, link)
	page.open()
	assert page.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_ADDED_TO_BASKET), "Message about successful product adding to basket should not be presented"

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
@pytest.mark.xfail(reason="bug")
def test_message_disappeared_after_adding_product_to_basket(browser, link):
	page = ProductPage(browser, link)
	page.open()
	page.add_product_to_basket()
	assert page.is_disappeared(*ProductPageLocators.MESSAGE_PRODUCT_ADDED_TO_BASKET), "Success message should be disappeared after adding product to basket"
