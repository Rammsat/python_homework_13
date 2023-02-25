from selene import have, be
from selene.support.shared import browser
from allure import step


def test_login(demoshop):
    with step('Открыть сайт'):
        demoshop.open('')
    with step('Логин должен быть выполен'):
        demoshop.element('.ico-logout').should(be.visible)


def test_logout(demoshop):
    with step('Открыть сайт'):
        demoshop.open('')
    with step('Сделать лог аут'):
        demoshop.element('.ico-logout').click()
    with step('Кнопка для логина должна быть видна'):
        demoshop.element('.ico-login').should(be.visible)


def test_add_product_to_basket(demoshop):
    with step('Открыть страницу товара'):
        demoshop.open('/build-your-cheap-own-computer')
    with step('Добавить товар в корзину'):
        demoshop.element('.add-to-cart-button').click()

    with step('Товар должен быть в корзине'):
        demoshop.element('.cart-qty').should(have.text('1'))


def test_add_to_compare_list(demoshop):
    with step('Открыть страницу товара'):
        demoshop.open('/build-your-cheap-own-computer')
    with step('Добавить товар к сравнению'):
        demoshop.element('.add-to-compare-list-button').click()

    with step('Кнопка для очистки списка сравнения должна быть видна'):
        browser.element(".clear-list").should(be.visible)


def test_search(demoshop):
    with step('Открыть сайт'):
        demoshop.open('')
    with step('Выполнить поиск'):
        demoshop.element('.search-box-text').type('Simple Computer').press_enter()

    with step('Товар должен быть найден'):
        browser.element(".product-title").should(have.exact_text('Simple Computer'))
