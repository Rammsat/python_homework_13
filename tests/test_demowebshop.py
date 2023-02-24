from selene import have, be
from selene.support.shared import browser


def test_login(demoshop):
    demoshop.open('')
    demoshop.element('.ico-logout').should(be.visible)


def test_logout(demoshop):
    demoshop.open('')
    demoshop.element('.ico-logout').click()
    demoshop.element('.ico-login').should(be.visible)


def test_add_product_to_basket(demoshop):
    demoshop.open('/build-your-cheap-own-computer')
    demoshop.element('.add-to-cart-button').click()

    demoshop.element('.cart-qty').should(have.text('1'))


def test_add_to_compare_list(demoshop):
    demoshop.open('/build-your-cheap-own-computer')
    demoshop.element('.add-to-compare-list-button').click()

    browser.element(".clear-list").should(be.visible)


def test_search(demoshop):
    demoshop.open('')
    demoshop.element('.search-box-text').type('Simple Computer').press_enter()

    browser.element(".product-title").should(have.exact_text('Simple Computer'))


